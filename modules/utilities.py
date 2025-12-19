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
    "topic_0":  "CI/CD",
    "topic_1":  "Transpiler Benchmarking",
    "topic_2":  "Rendering and Data Loading",
    "topic_3":  "Timeout and Concurrency",
    "topic_4":  "Sequence Data Processing",
    "topic_5":  "Join Query",
    "topic_6":  "Network Call Optimization",
    "topic_7":  "Dependency Management",
    "topic_8":  "Performance Benchmarking",
    "topic_9":  "Memory Leak",
    "topic_10": "Constant Folding",
    "topic_11": "CLI Tool",
    "topic_12": "Frontend Page Loading",
    "topic_13": "Smoke Tests",
    "topic_14": "Collection Reuse",
    "topic_15": "VM",
    "topic_16": "Token Usage",
    "topic_17": "Streamline Build",
    "topic_18": "Compiler Runtime",
    "topic_19": "Caching for APIs",
    "topic_20": "Compiler Output",
    "topic_21": "Group by Query in Compiler ",
    "topic_22": "Caching Control",
    "topic_23": "Large Workload Performance",
    "topic_24": "Bundle Size",
    "topic_25": "Builtin Optimization in Compiler  ",
    "topic_26": "SIMD Optimization",
    "topic_27": "Benchmark Update",
    "topic_28": "Debouncing",
    "topic_29": "Query",
    "topic_30": "File and Data Handling",
    "topic_31": "HTTP",
    "topic_32": "Report Generation Process",
    "topic_33": "Collection and Hashing",
    "topic_34": "Telemetry and Tracing",
    "topic_35": "Offline Asset Caching",
    "topic_36": "N+1 Query Optimization",
    "topic_37": "Cache Constraints",
    "topic_38": ".NET Build",
    "topic_39": "Transpiler Functionality",
    "topic_40": "Timeout",
    "topic_41": "UI Improvement",
    "topic_42": "VM Register",
    "topic_43": "Hash Generation",
    "topic_44": "GPU Usage",
    "topic_45": "Caching Logic",
    "topic_46": "Scheduling",
    "topic_47": "Bytecode",
    "topic_48": "Chat System",
    "topic_49": "Backend Query",
    "topic_50": "Redundant Processing",
    "topic_51": "GPU"
}

category_map = {
    "Development": [
        "topic_0",   # CI/CD Workflow
        "topic_7",   # Dependency Management
        "topic_11",  # CLI tool
        "topic_13",  # Smoke Tests
        "topic_17",  # Streamline Build
        "topic_38",  # .NET build
        "topic_40",  # Test Timeout
    ],

    "Low-level": [
        "topic_1",   # Transpiler Benchmarking
        "topic_10",  # Constant Folding
        "topic_14",  # Collection Reuse
        "topic_15",  # VM Constant Folding
        "topic_18",  # Compiler Runtime
        "topic_20",  # Compiler improvement for Output
        "topic_21",  # Group-by in Compiler
        "topic_25",  # Builtin Optimization in Compiler
        "topic_26",  # Kernel Usage Optimization
        "topic_39",  # Transpiler Improvement for Output
        "topic_42",  # VM Register
        "topic_47",  # Go Compiler
    ],

    "UI": [
        "topic_2",   # UI Data-loading and Rendering
        "topic_12",  # UI loading and Rendering
        "topic_24",  # Bundle Size
        "topic_28",  # Responsive UI
        "topic_30",  # File Scanning for UI
        "topic_41",  # Redundant UI Update
    ],

    "Caching": [
        "topic_3",   # TTL approximation
        "topic_22",  # Caching Control
        "topic_35",  # Offline Asset Caching
        "topic_45",  # Caching Expiry
    ],

    "Algorithmic": [
        "topic_4",   # Sequence Data Processing
        "topic_23",  # Large Workload
        "topic_33",  # Hashing
        "topic_36",  # N+1 Query Optimization
        "topic_43",  # Hash Generation
        "topic_46",  # Scheduling
        "topic_50",  # Redundant Function Call
    ],

    "Query": [
        "topic_5",   # Join Query
        "topic_29",  # Query Execution
        "topic_49",  # Backend Query Update
    ],

    "Networking": [
        "topic_6",   # Networking & I/O
        "topic_19",  # HTTP Payload Caching
        "topic_31",  # HTTP Client
        "topic_32",  # DTO
        "topic_37",  # Rate Limiting
    ],

    "Monitoring and Evaluation": [
        "topic_8",   # Performance Benchmarking
        "topic_27",  # Benchmark Update
        "topic_34",  # Telemetry and tracing
    ],

    "Hardware": [
        "topic_9",   # Memory Leak
        "topic_44",  # GPU Usage
        "topic_51",  # GPU Acceleration
    ],

    "AI": [
        "topic_16",  # LLM Token Usage
        "topic_48",  # Chat API
    ],
}
