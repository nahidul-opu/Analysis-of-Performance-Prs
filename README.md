
## Setup
1. create virtual environment: virtualenv .venv
2. pip install -r requirements.txt
3. git clone https://huggingface.co/datasets/hao-li/AIDev


## Project Structure

```
MSR-MiningChallenge26/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── AIDev/                             # Cloned dataset repository
├── modules/                           # Reusable Python modules
│   ├── __init__.py
│   ├── CliffsDelta.py                 # Effect size calculation module
│   ├── constants.py                   # Constants and mappings
│   ├── evaluate_bertopic.py           # BERTopic evaluation utilities
│   ├── text_classifiers.py            # Text classification utilities
│   ├── text_preprocessor.py           # Text preprocessing utilities
│   ├── utilities.py                   # General utility functions
├── Outputs/                           # Analysis results and visualizations
│   ├── llm_filtered.csv               # LLM-filtered results
│   ├── BERTopic/                      # BERTopic model outputs
│   │   ├── All_PR_Topics.csv
│   │   ├── Topic_Info.csv
│   │   └── Topics/                    # Individual topic files (topic_*.csv)
│   ├── Embeddings/                    # Pre-computed embeddings
│   │   └── Qwen8Embeddings.npy
│   ├── Figures/                       # Generated visualizations (PDF)
│   └── PerformancePRs/                # Performance PR datasets
│       ├── HUMAN_PULL_Requests_llm_filtered.csv
│       ├── POP_PULL_Requests_*.csv
│       └── ManuallyValidated/         # Manually validated samples
├── RQ1.ipynb                          # Research Question 1
├── RQ2.ipynb                          # Research Question 2
├── RQ3.ipynb                          # Research Question 3
├── TopicModeling.ipynb                # Topic Modeling with BERTopic
├── Analysis.ipynb                     # Keyword base filtering and other analysis 
├── filter.py                          # Use LLM to classify PR (Performance vs Non-Performance)
├── Run.sh                             # Run SLURM job to use LLM for classification
```

## Notebooks Description

Each notebook loads harmonized PR datasets from `Outputs/PerformancePRs/` (plus the BERTopic exports under `Outputs/BERTopic/`) and writes refreshed figures back into `Outputs/Figures/`. They share helper functions from `modules/` so the code paths stay consistent across experiments.


### TopicModeling.ipynb
BERTopic modeling with Qwen3-Embedding-8b, UMAP, HDBSCAN and constraint grid search. 

### RQ1.ipynb – Topics and Categories
***What categories of performance optimizations do agentic AIs address?***

We identified 52 performance topics grouped into 10 categories, ranging from low-level optimizations to UI- and AI-related concerns, showing that agentic AIs operate across multiple stack layers.

### RQ2.ipynb – Acceptance Rate and Merge time
How do PR rejection rates and review times vary across categories?

We observed an overall rejection rate of 36.5\% in performance-related PRs, which is significantly higher than in non-performance PRs (22.7\%). Also, rejection rates and review latency are largely driven by the type of performance concern, with agents performing worst on UI, AI, and Analytics PRs.

### RQ3.ipynb – Association with SDLC Activities
What SDLC activities are associated with AI-generated performance-related PRs?

We found that performance-related PRs are more associated with feature implementation (i.e., development activities) and comparatively less associated with bug fixes, refactoring, and testing. This may indicate a potential gap in AI-assisted performance optimization during the maintenance ph
