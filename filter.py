# %%

import os
from tqdm import tqdm
import pandas as pd
from modules.constants import *
from modules.utilities import *
from modules.text_classifiers import *

random_state = 5

# %%
os.makedirs(OUTPUT_DIR, exist_ok=True)


# %%
def filter_performance_topics(filename, columns, preprocessor, classifier, callback, skip = 0):
    df = read_aidev(filename)
    output_rows = []

    count = 0

    for _, row in tqdm(df.iterrows()):
        count = count + 1
        
        if count < skip:
            continue
        
        text = ""

        try:
            for col in columns:
                if isinstance(row[col], str):
                    if text != "":
                        text += "\n"

                    val = row[col]
                    if preprocessor is not None:
                        val = preprocessor.preprocess(val)

                    text += val

            if text and text != "" and classifier.classify(text):
                row = row.copy()

                if isinstance(classifier, RegexClassifier) or isinstance(classifier, SimpleSubstringClassifier):
                    row["matched_words"] = classifier.get_matches()
                elif isinstance(classifier, LLMClassifier):
                    row["llm_output"] = classifier.get_prediction()
                elif isinstance(classifier, EmbeddingClassifier):
                    row["probability"] = classifier.get_score()

                output_rows.append(row)
            
            callback(pd.DataFrame(output_rows))
        except Exception as e:
            print(f"Error on {count}th: " , e)

    output_df = pd.DataFrame(output_rows)

    return output_df


# %%

def save(df):
    df.to_csv(os.path.join(OUTPUT_DIR, "llm_filtered.csv"), index=False)

filename = FileName.ALL_PULL_REQUEST
columns = ["title", "body"]

keywords = set(
    [
        "performance",
        "compile-time-hog",
        "perf",
        "hang",
        "optimization",
        "responsive",
        "slow",
        "speed",
        "latency",
        "throughput",
        "wait",
        "slow",
        "fast",
        "lag",
        "tim",
        "minor",
        "stuck",
        "instant",
        "respons",
        "react",
        "speed",
        "latenc",
        "perform",
        "throughput",
        "hang",
        "memory",
        "leak",
    ]
)
base_text = ", ".join(keywords)
prompt = [
    {
        "role": "system",
        "content": "You are a GitHub Pull Request Classification Agent. Given a text combining the title and body of a pull request, determine whether the primary purpose of the pull request is to improve performance. Classify each pull request as either 'performance' or 'non-performance'. Performance-related pull requests may contain keywords such as "
        + ", ".join(keywords) + ", or any other terms referring to how faster and efficiently software runs.",
    }
]
classifier = LLMClassifier(prompt)
preprocessor = None

df = filter_performance_topics(filename, columns, preprocessor, classifier, save, 0)