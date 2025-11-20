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
        if count < skip:
            continue
        
        count = count + 1
        
        text = ""
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
        "content": "You are a text-classification agent. Analyze the given text and determine whether it discusses software performance. Answer 'performance' or 'non-performance' accordingly. Performance-related text may contain keywords such as "
        + ", ".join(keywords) + ", or any other terms referring to how efficiently software runs.",
    }
]
classifier = LLMClassifier(prompt)
preprocessor = None

df = filter_performance_topics(filename, columns, preprocessor, classifier, save)
