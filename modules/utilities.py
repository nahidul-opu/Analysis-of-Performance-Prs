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


topic_map = {
    "topic_0": "",
    "topic_1": "",
    "topic_2": "",
    "topic_3": "",
    "topic_4": "",
    "topic_5": "",
    "topic_6": "",
    "topic_7": "",
    "topic_8": "",
    "topic_9": "",
    "topic_10": "",
    "topic_11": "",
    "topic_12": "",
    "topic_13": "",
    "topic_14": "",
    "topic_15": "",
    "topic_16": "",
    "topic_17": "",
    "topic_18": "",
    "topic_19": "",
    "topic_20": "",
    "topic_21": "",
    "topic_22": "",
    "topic_23": "",
    "topic_24": "",
    "topic_25": "",
    "topic_26": "",
    "topic_27": "",
    "topic_28": "",
    "topic_29": "",
    "topic_30": "",
    "topic_31": "",
    "topic_32": "",
    "topic_33": "",
    "topic_34": "",
    "topic_35": "",
    "topic_36": "",
    "topic_37": "",
    "topic_38": "",
    "topic_39": "",
    "topic_40": "",
    "topic_41": "",
    "topic_42": "",
    "topic_43": "",
    "topic_44": "",
    "topic_45": "",
    "topic_46": "",
    "topic_47": "",
    "topic_48": "",
    "topic_49": "",
    "topic_50": "",
    "topic_51": ""
}
