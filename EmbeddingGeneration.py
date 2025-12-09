import pandas as pd
import numpy as np
import regex as re

import os

from bs4 import BeautifulSoup
from markdown import markdown
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

from bertopic.representation import KeyBERTInspired, PartOfSpeech, MaximalMarginalRelevance
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.dimensionality import BaseDimensionalityReduction
from bertopic.vectorizers import ClassTfidfTransformer
from hdbscan import HDBSCAN
from umap import UMAP

from modules.constants import *

seed = 42

def markdown_to_text(markdown_string):
    """ Converts a markdown string to plaintext """

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    return text

def clean_text(text):
    text = markdown_to_text(text).strip()

    text = text.lower()

    for agent in AGENTS:
        text = text.replace(agent.lower(), "")

    text = re.sub(r"http\S+", " <URL> ",text) #Removing URLs 
    
    # html=re.compile(r'<.*?>') 
    
    # text = html.sub(r'',text) #Removing html tags
    
    emoji_pattern = re.compile("["
                               "\U0001F600-\U0001F64F"  # Emoticons
                               "\U0001F300-\U0001F5FF"  # Symbols & pictographs
                               "\U0001F680-\U0001F6FF"  # Transport & map symbols
                               "\U0001F700-\U0001F77F"  # Alchemical symbols
                               "\U0001F780-\U0001F7FF"  # Geometric shapes
                               "\U0001F800-\U0001F8FF"  # Supplemental arrows
                               "\U0001F900-\U0001F9FF"  # Supplemental symbols and pictographs
                               "\U0001FA00-\U0001FA6F"  # Symbols and pictographs extended-A
                               "\U0001FA70-\U0001FAFF"  # Symbols and pictographs extended-B
                               "\U00002702-\U000027B0"  # Dingbats
                               "\U000024C2-\U0001F251"  # Enclosed characters
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text) #Removing emojis
    #common_punctuation = r'.,?!:;"\'-\\/'
    #text = re.sub(rf'[^\w\s{re.escape(common_punctuation)}]', '', text)
    #text = re.sub(r'\s+', ' ', text).strip()
    return text

model = SentenceTransformer("Qwen/Qwen3-Embedding-8B", device="cuda:0")

os.makedirs("Outputs/Embeddings", exist_ok=True)

df_ai = pd.read_csv("Outputs/PerformancePRs/POP_PULL_Requests_LLM_filtered.csv")
df_ai["title"] = df_ai["title"].fillna("").apply(lambda x: clean_text(x))
df_ai["body"] = df_ai["body"].fillna("").apply(lambda x: clean_text(x))

data_title = df_ai["title"]
data_body = df_ai["body"]

prompt_title = """Extract the performance-related meaning of this pull request title.
Focus on:
- What performance issue it implies
- The type of optimization suggested
- Whether it hints at improving speed, efficiency, memory, or scalability"""

prompt_body = """Extract and represent the core meaning of how this PR improves performance.
Focus on:
- The performance issue addressed
- The optimization introduced
- Why it improves speed, efficiency, memory, or scalability
- Any benchmark or improvement hints"""

embeddings_title = model.encode(
                data_title,
                prompt = prompt_title
            )
embeddings_body = model.encode(
                data_body,
                prompt = prompt_body
            )

np.save("./Outputs/Embeddings/Qwen8Embeddings_title.npy", embeddings_title)
np.save("./Outputs/Embeddings/Qwen8Embeddings_body.npy", embeddings_body)