# %%

import os
from tqdm import tqdm

from modules.constants import *
from modules.utilities import *
from modules.text_classifiers import *

random_sate = 5

# %%
os.makedirs(OUTPUT_DIR, exist_ok=True)


# %%
def filter_performance_topics(filename, columns, preprocessor, classifier):
    df = read_aidev(filename)
    output_rows = []

    for _, row in tqdm(df.iterrows()):
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
            output_rows.append(row)
            try:
                row["matched_words"] = classifier.get_matches()
            except:
                pass

    output_df = pd.DataFrame(output_rows)

    return output_df


# %%

filename = FileName.POP_ISSUE
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

df = filter_performance_topics(filename, columns, preprocessor, classifier)
df.to_csv(os.path.join(OUTPUT_DIR, "llm_filtered.csv"), index=False)
