# %% [markdown]
# # Imports

# %%
import pandas as pd
import numpy as np
import regex as re
import itertools
import os


from bs4 import BeautifulSoup
from markdown import markdown
from swifter import swifter
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

from bertopic.representation import KeyBERTInspired, PartOfSpeech, MaximalMarginalRelevance
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.dimensionality import BaseDimensionalityReduction
from bertopic.vectorizers import ClassTfidfTransformer
from hdbscan import HDBSCAN
from umap import UMAP

from modules.evaluate_bertopic import evaluate_topics
from modules.constants import *
from modules.utilities import read_aidev

seed = 42

# %% [markdown]
# # Load Data

# %%
# df = pd.read_csv("Outputs/PerformancePRs/POP_PULL_Requests_LLM_filtered.csv")

# df_pr_type = read_aidev(FileName.POP_PR_TASK_TYPE)
# df_pr_type = df_pr_type[df_pr_type["type"] == "perf"]

# df_pop_all = read_aidev(FileName.POP_PULL_REQUEST)

# pr_type_ids = df_pr_type["id"].tolist()
# perf_pr_ids = df["id"].tolist()

# cnt = 0
# ids = []
# for id in pr_type_ids:
#     if id not in perf_pr_ids:
#         cnt += 1
#         perf_pr_ids.append(id)

# print(f"{cnt} PRs not found in our list")

# df = df_pop_all[df_pop_all["id"].isin(perf_pr_ids)]

# df.to_csv("Outputs/PerformancePRs/POP_PULL_Requests_LLM_filtered_final.csv", index = False)

# %%
df = pd.read_csv("Outputs/PerformancePRs/POP_PULL_Requests_LLM_filtered_final.csv")


# %%
data_title = df["title"].fillna("")
data_body = df["body"].fillna("")

data_title = df["title"].tolist()
data_body = df["body"].tolist()

docs = [str(i) + "\n" + str(j) for i, j in zip(data_title, data_body)]

# %% [markdown]
# # Embedding Generation

# %%
model = SentenceTransformer("Qwen/Qwen3-Embedding-8B", device="cuda:0")

# %%
embeddings = model.encode(docs, batch_size = 4, show_progress_bar = True)

np.save("Qwen8PlainEmbeddings.npy",embeddings)

# %% [markdown]
# # UMAP

# %%
embeddings = np.load("./Outputs/Embeddings/Qwen8Embeddings.npy")

# %%
n_component = 50
n_neighbors = 3

umap_model = UMAP(n_neighbors=n_neighbors, n_components=n_component, min_dist=0.1, metric='cosine', random_state=seed)
embeddings_reduced = umap_model.fit_transform(embeddings)


# %% [markdown]
# # BERTopic

# %%
os.makedirs("Outputs/BERTopic", exist_ok=True)

# %%
hdbscan_model = HDBSCAN(min_cluster_size=10, min_samples=1, cluster_selection_epsilon=0.1, metric="euclidean", prediction_data=True)

ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
vectorizer_model = CountVectorizer(stop_words= "english", ngram_range=(1, 2), min_df=1)
representation_model = [KeyBERTInspired(), MaximalMarginalRelevance(diversity=0.3)]

# %%
topic_model = BERTopic(
    embedding_model=model,
    umap_model=BaseDimensionalityReduction(),
    hdbscan_model=hdbscan_model,
    vectorizer_model=vectorizer_model,
    representation_model=representation_model,
    ctfidf_model=ctfidf_model,
    calculate_probabilities=True,
    top_n_words=10,
    verbose=True,
)

topics, probs = topic_model.fit_transform(docs, embeddings=embeddings_reduced)
topic_info_df = topic_model.get_topic_info()
topic_info_df

# %%
topic_df = topic_model.get_document_info(docs)
df["Topic"] = topic_df["Topic"]
df["Probability"] = topic_df["Probability"]
df["Representative_document"] = topic_df["Representative_document"]
df

# %%
topic_info_df.to_csv("./Outputs/BERTopic/Topic_Info.csv", index = False)
df.to_csv("./Outputs/BERTopic/All_PR_Topics.csv", index = False)

# %%
os.makedirs("./Outputs/BERTopic/Topics", exist_ok=True)

for topic in topic_info_df["Topic"].tolist():
    df_topic = df[df["Topic"] == topic]
    df_topic = df_topic.sort_values("Probability", ascending=False)
    df_topic.to_csv(f"./Outputs/BERTopic/Topics/topic_{topic}.csv", index = False)
    print(f"{topic} : {df_topic.shape[0]}")

# %% [markdown]
# # Parameter Tuning

# %%
embeddings_combined = np.load("./Outputs/Embeddings/Qwen8Embeddings.npy")

# %%
def bertopic_grid_search(
    docs,
    embeddings,
    umap_params_grid,
    hdbscan_params_grid,
    vectorizer_params_grid=None
):
    """
    Perform grid search over UMAP, HDBSCAN, and vectorizer parameters
    using BERTopic + evaluation_metrics from evaluate_topics module.
    """

    all_results = []
    best_score = -999
    best_model = None
    best_config = None

    total_combinations = (
            len(umap_params_grid) *
            len(hdbscan_params_grid) *
            len(vectorizer_params_grid)
        )

    for umap_params, hdb_params, vect_params in tqdm(itertools.product(umap_params_grid, hdbscan_params_grid, vectorizer_params_grid),
        total=total_combinations,
        desc="Parameter search"
        ):

        # print("\n==============================")
        # print("Testing configuration:")
        # print("UMAP:", umap_params)
        # print("HDBSCAN:", hdb_params)
        # print("Vectorizer:", vect_params)
        # print("==============================")
        try:
        # 1. Build UMAP
            umap_model = UMAP(
                n_neighbors=umap_params.get("n_neighbors", 15),
                n_components=umap_params.get("n_components", 10),
                min_dist=umap_params.get("min_dist", 0.1),
                metric=umap_params.get("metric", "cosine"),
                random_state=seed
            )

            reduced_embeddings = umap_model.fit_transform(embeddings)

            # 2. Build HDBSCAN
            hdbscan_model = HDBSCAN(
                min_cluster_size=hdb_params.get("min_cluster_size", 10),
                min_samples=hdb_params.get("min_samples", 1),
                cluster_selection_epsilon=hdb_params.get("cluster_selection_epsilon", 0.1),
                metric=hdb_params.get("metric", "euclidean"),
                prediction_data=True
            )

            # 3. Build vectorizer
            vectorizer_model = CountVectorizer(
                stop_words="english",
                ngram_range=vect_params.get("ngram_range", (1, 2)),
                min_df=vect_params.get("min_df", 1)
            )

            ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
            representation_model = [MaximalMarginalRelevance(diversity=0.3)]

            # 4. Train BERTopic
            topic_model = BERTopic(

                embedding_model=None,    # using precomputed embeddings
                umap_model=BaseDimensionalityReduction(),
                hdbscan_model=hdbscan_model,
                vectorizer_model=vectorizer_model,
                ctfidf_model=ctfidf_model,
                representation_model=representation_model,
                calculate_probabilities=True,
                verbose=False
            )

            topics, probs = topic_model.fit_transform(docs, embeddings=reduced_embeddings)

            # 5. Evaluate
            metrics = evaluate_topics(topic_model, docs, reduced_embeddings)

            coherence = metrics["coherence"]
            diversity = metrics["diversity"]
            silhouette = metrics["silhouette"]

            try:
                score = coherence + silhouette # Weighted score (adjust as needed)
            except:
                score = 0

            all_results.append({
                "umap": umap_params,
                "hdbscan": hdb_params,
                "vectorizer": vect_params,
                "coherence": coherence,
                "diversity": diversity,
                "silhouette": silhouette,
                "num_clusters": metrics["cluster_metrics"]["num_clusters"],
                "outliers_pct": metrics["cluster_metrics"]["outlier_percentage"],
                "score": score,
                "model": topic_model
            })

            if score > best_score:
                best_score = score
                best_model = topic_model
                best_config = (umap_params, hdb_params, vect_params)
        except:
            pass

    # Convert results to DataFrame (excluding model objects)
    df_results = pd.DataFrame([
        {k: v for k, v in r.items() if k != "model"} 
        for r in all_results
    ])

    return best_model, best_config, df_results


# %%
umap_grid = [

    {"n_components": 10, "n_neighbors": 3},
    {"n_components": 10, "n_neighbors": 5},

    {"n_components": 20, "n_neighbors": 3},
    {"n_components": 20, "n_neighbors": 5},

    {"n_components": 50, "n_neighbors": 3},
    {"n_components": 50, "n_neighbors": 5},

    {"n_components": 100, "n_neighbors": 3},
    {"n_components": 100, "n_neighbors": 5},
]

hdbscan_grid = [
    {"min_cluster_size": 5, "min_samples": 1},
    {"min_cluster_size": 10, "min_samples": 1},
    {"min_cluster_size": 15, "min_samples": 1},
]

vectorizer_grid = [
    {"ngram_range": (1, 2)},
]

best_model, best_config, results_df = bertopic_grid_search(docs, embeddings_combined, umap_grid, hdbscan_grid, vectorizer_grid)

print("\nBEST CONFIGURATION:")
print(best_config)


# %%
results_df


