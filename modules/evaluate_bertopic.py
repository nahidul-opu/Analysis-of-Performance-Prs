import logging
from collections import Counter
from typing import List, Optional, Dict, Any

import numpy as np
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from sklearn.metrics import silhouette_score

# If you rely on BERTopic, import its types only for annotations (optional)
# from bertopic import BERTopic

logger = logging.getLogger(__name__)


def _get_valid_topic_ids(topic_model) -> List[int]:
    """
    Return a list of topic ids produced by BERTopic excluding the noise topic (-1).
    Uses get_topic_info() which is a stable way to obtain topic ids and their counts.
    """
    try:
        topic_info = topic_model.get_topic_info()
        # topic_info is a DataFrame with a 'Topic' column
        topic_ids = [int(t) for t in topic_info.Topic.tolist() if int(t) != -1]
        return topic_ids
    except Exception:
        # Fallback: try to use topics_ attribute (list of topic ids per document)
        # and get unique topics from it
        try:
            topics_list = getattr(topic_model, "topics_", None)
            if topics_list is None:
                return []
            return sorted(set([int(t) for t in topics_list if int(t) != -1]))
        except Exception:
            return []


def compute_topic_coherence(topic_model, docs: List[str], top_n: int = 10) -> Optional[float]:
    """
    Compute c_v coherence using gensim's CoherenceModel.

    Parameters
    ----------
    topic_model : BERTopic instance or similar object exposing get_topic(topic_id) and get_topic_info()
    docs : list[str]
        Raw documents (strings). Tokenization will be naive whitespace split; if you already have preprocessed
        tokens, pass them in as `'docs'` or modify this function.
    top_n : int
        Number of top words to use per topic.

    Returns
    -------
    float | None
        c_v coherence score or None if it could not be computed.
    """
    if not docs:
        logger.warning("Empty docs provided to compute_topic_coherence.")
        return None

    # Basic tokenization. If you have pre-tokenized input, skip this step.
    tokenized_docs = []
    for d in docs:
        if d is None:
            tokenized_docs.append([])
        else:
            tokenized_docs.append(str(d).split())

    try:
        dictionary = Dictionary(tokenized_docs)
        corpus = [dictionary.doc2bow(text) for text in tokenized_docs]
    except Exception as exc:
        logger.exception("Failed to build gensim Dictionary/corpus: %s", exc)
        return None

    # Build topic_words using BERTopic-safe API
    topic_ids = _get_valid_topic_ids(topic_model)
    if not topic_ids:
        logger.warning("No topics found in topic_model for coherence computation.")
        return None

    topic_words = []
    for topic_id in topic_ids:
        try:
            # get_topic(topic_id) returns list[(word, score), ...]
            top_terms = topic_model.get_topic(topic_id)
            if not top_terms:
                continue
            words = [w for w, _ in top_terms[:top_n]]
            if words:
                topic_words.append(words)
        except Exception:
            logger.exception("Failed to extract words for topic id %s", topic_id)
            continue

    if not topic_words:
        logger.warning("No topic words available for coherence calculation.")
        return None

    try:
        coherence_model = CoherenceModel(
            topics=topic_words,
            texts=tokenized_docs,
            dictionary=dictionary,
            coherence="c_v",
        )
        return float(coherence_model.get_coherence())
    except Exception:
        logger.exception("Gensim CoherenceModel failed.")
        return None


def compute_topic_diversity(topic_model, top_k: int = 10) -> float:
    """
    Compute topic diversity: number of unique words in top_k of each topic divided by (num_topics * top_k).
    This is the standard formula used widely: unique_words / (num_topics * top_k)
    Returns 0.0 if no topics or no words found.
    """
    topic_ids = _get_valid_topic_ids(topic_model)
    if not topic_ids:
        return 0.0

    all_words = []
    for topic_id in topic_ids:
        try:
            top_terms = topic_model.get_topic(topic_id)
            if not top_terms:
                continue
            words = [w for w, _ in top_terms[:top_k]]
            all_words.extend(words)
        except Exception:
            logger.exception("Failed to get topic %s for diversity computation.", topic_id)
            continue

    total_slots = len(topic_ids) * top_k
    if total_slots == 0:
        return 0.0

    unique_words = len(set(all_words))
    return unique_words / float(total_slots)


def compute_hdbscan_metrics(hdbscan_model) -> Dict[str, Any]:
    """
    Extract HDBSCAN cluster statistics and stability indicators.
    If hdbscan_model is None, returns empty/zeroed metrics.
    """
    if hdbscan_model is None:
        return {
            "num_clusters": 0,
            "num_outliers": 0,
            "outlier_percentage": 0.0,
            "cluster_sizes": {},
            "cluster_stability": None,
        }

    labels = getattr(hdbscan_model, "labels_", None)
    if labels is None:
        # Some BERTopic setups won't expose hdbscan directly; return safe defaults
        return {
            "num_clusters": 0,
            "num_outliers": 0,
            "outlier_percentage": 0.0,
            "cluster_sizes": {},
            "cluster_stability": getattr(hdbscan_model, "cluster_persistence_", None),
        }

    labels = list(labels)
    total = len(labels)
    n_outliers = labels.count(-1)
    # unique cluster ids excluding -1
    cluster_ids = set(labels) - {-1}
    n_clusters = len(cluster_ids)

    # Compute sizes excluding outliers or include -1 depending on desired view
    cluster_sizes = {int(k): int(v) for k, v in Counter(labels).items()}

    stability = getattr(hdbscan_model, "cluster_persistence_", None)

    outlier_percentage = round((n_outliers / total * 100) if total > 0 else 0.0, 2)

    return {
        "num_clusters": n_clusters,
        "num_outliers": n_outliers,
        "outlier_percentage": outlier_percentage,
        "cluster_sizes": cluster_sizes,
        "cluster_stability": stability,
    }


def compute_silhouette(embeddings, labels) -> Optional[float]:
    """
    Compute silhouette score only on non-outlier points (labels != -1).
    Validate shapes / sizes and return None if not computable.
    """
    if embeddings is None or labels is None:
        logger.debug("Embeddings or labels are None; skipping silhouette.")
        return None

    emb = np.asarray(embeddings)
    lab = np.asarray(labels)

    if emb.shape[0] != lab.shape[0]:
        logger.warning(
            "Embeddings length (%s) and labels length (%s) differ; cannot compute silhouette.",
            emb.shape[0],
            lab.shape[0],
        )
        return None

    valid_idx = lab != -1
    if np.sum(valid_idx) <= 1:
        logger.info("Not enough non-outlier points for silhouette (need at least 2).")
        return None

    unique_labels = set(lab[valid_idx].tolist())
    if len(unique_labels) <= 1:
        logger.info("Silhouette requires at least 2 clusters (excluding outliers).")
        return None

    try:
        return float(silhouette_score(emb[valid_idx], lab[valid_idx]))
    except Exception:
        logger.exception("Failed to compute silhouette score.")
        return None


def evaluate_topics(
    topic_model,
    docs: List[str],
    embeddings: Optional[np.ndarray] = None,
    top_n_coherence: int = 10,
    top_k_diversity: int = 10,
    verbose: bool = False,
) -> Dict[str, Any]:
    """
    Full evaluation pipeline for BERTopic-style topic models.

    Parameters
    ----------
    topic_model : BERTopic instance
    docs : list[str]
    embeddings : np.ndarray | None
        Document embeddings aligned with the topic assignments (same order/length as docs).
    top_n_coherence : int
        Number of top words per topic to consider for coherence.
    top_k_diversity : int
        Number of top words per topic to consider for diversity.
    verbose : bool
        If True, prints progress to stdout. Otherwise uses logging.

    Returns
    -------
    dict
        Results containing coherence, diversity, cluster_metrics, silhouette score.
    """
    if verbose:
        print("\n=== BERTopic Evaluation ===")

    # 1. Coherence
    if verbose:
        print("Computing topic coherence (c_v)...")
    coherence = compute_topic_coherence(topic_model, docs, top_n=top_n_coherence)
    if verbose:
        print("Topic Coherence (c_v):", coherence)

    # 2. Diversity
    if verbose:
        print("Computing topic diversity...")
    diversity = compute_topic_diversity(topic_model, top_k=top_k_diversity)
    if verbose:
        print("Topic Diversity:", diversity)

    # 3. HDBSCAN Metrics
    if verbose:
        print("Checking HDBSCAN cluster statistics...")
    # Prefer hdbscan from the model; fallback to None
    hdbscan_model = getattr(topic_model, "hdbscan_model", None)
    cluster_stats = compute_hdbscan_metrics(hdbscan_model)

    if verbose:
        print("Clusters:", cluster_stats["num_clusters"])
        print("Outlier %:", cluster_stats["outlier_percentage"])
        print("Cluster sizes:", cluster_stats["cluster_sizes"])
        print("Cluster stability:", cluster_stats["cluster_stability"])

    # 4. Silhouette Score
    silhouette = None
    # Try to obtain labels: prefer hdbscan_model.labels_, else topic_model.topics_
    labels = None
    if embeddings is not None:
        if hdbscan_model is not None and getattr(hdbscan_model, "labels_", None) is not None:
            labels = hdbscan_model.labels_
        else:
            labels = getattr(topic_model, "topics_", None)

    if embeddings is not None and labels is not None:
        if verbose:
            print("Computing silhouette score...")
        silhouette = compute_silhouette(embeddings, labels)
        if verbose:
            print("Silhouette Score:", silhouette)
    elif embeddings is not None and labels is None:
        logger.warning("Embeddings provided but could not obtain labels from topic_model/hdbscan_model.")

    if verbose:
        print("\n=== Evaluation Complete ===")

    return {
        "coherence": coherence,
        "diversity": diversity,
        "cluster_metrics": cluster_stats,
        "silhouette": silhouette,
    }
