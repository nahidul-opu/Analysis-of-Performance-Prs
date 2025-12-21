# MSR-MiningChallenge26

## Setup
1. create virtual environment: virtualenv .venv
2. pip install -r requirements.txt
3. git clone https://huggingface.co/datasets/hao-li/AIDev

## Update requirements.txt
```
python -m pip freeze -l > requirements.txt
```
- Delete windows or OS specific requirements from the file (Eg., pywinpty)

## Run tests
```
python -m unittest discover -s tests  
```

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
├── RQ1.ipynb                          # Research Question 1: Topic Distribution
├── RQ2.ipynb                          # Research Question 2: PR Acceptance Analysis
├── RQ3.ipynb                          # Research Question 3: Time to Merge & Changes
├── RQ4.ipynb                          # Research Question 4: Agent Performance
└── RQ5.ipynb                          # Research Question 5: PR Task Types

```

## Notebooks Description

### RQ1.ipynb - Topic Distribution Analysis
Analyzes the distribution of Pull Requests across identified topics using BERTopic model outputs. Creates visualizations showing:
- Topic distribution with percentages
- Performance optimization hierarchy
- Performance PR tree structure

### RQ2.ipynb - PR Acceptance Analysis
Examines acceptance/rejection rates of Performance PRs across different categories. Produces:
- Stacked bar charts showing accepted vs rejected PRs
- Statistical analysis by category
- Agent-based performance metrics

### RQ3.ipynb - Time to Merge & Code Changes Analysis
Investigates temporal and code change metrics for PRs:
- Time-to-merge distribution by category (boxplots)
- Total changes by category
- Kendall tau correlation between changes and merge time
- Statistical testing (Shapiro-Wilk, Wilcoxon Rank-Sum, Cliff's Delta)

### RQ4.ipynb - Agent Performance Comparison
Compares performance across different AI agents:
- Polar radar charts showing agent distribution across categories
- Analysis of accepted PRs by agent
- Agent-wise performance metrics

### RQ5.ipynb - PR Task Types Analysis
Analyzes different types of tasks/commits in Performance PRs:
- Stacked bar charts showing feat/fix/refactor/test/docs/ci/build/chore distribution
- Breakdown by category and agent
- Task type composition analysis

