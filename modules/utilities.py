import pandas as pd

from modules.constants import *

COLOR_MAP = {
    "Human": "#56B4E9",
    "OpenAI_Codex": "#D55E00",
    "OpenAI Codex": "#D55E00",
    "Codex": "#F0E442",
    "Devin": "#009E73",
    "Copilot": "#0072B2",
    "GitHub Copilot": "#0072B2",
    "Cursor": "#785EF0",
    "Claude_Code": "#DC267F",
    "Claude Code": "#DC267F",
}


# –– Nature-ready styling
mpl_params = {
        "font.family": "DeJavu Serif",
        "font.serif": ["Times New Roman", "Times"],
        "mathtext.fontset": "stix",
        "axes.linewidth": 1.0,
        "axes.labelsize": 14,
        "axes.titlesize": 14,
        "xtick.major.size": 4,
        "ytick.major.size": 4,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "legend.fontsize": 14,
        "legend.title_fontsize": 14,
        "figure.dpi": 300,
    }

def read_aidev(name):
    return pd.read_parquet(AIDEV_DATA_DIR + name + ".parquet")