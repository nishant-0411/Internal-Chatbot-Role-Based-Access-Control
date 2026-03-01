from pathlib import Path
import json
import re
from collections import defaultdict
from app.core.logger import logger

INDEX_PATH = Path("page_index")
PAGE_STORE_FILE = INDEX_PATH / "page_store.json"
INVERTED_INDEX_FILE = INDEX_PATH / "inverted_index.json"
METADATA_INDEX_FILE = INDEX_PATH / "metadata_index.json"
IDF_INDEX_FILE = INDEX_PATH / "idf_index.json"

with open(PAGE_STORE_FILE, 'r', encoding="utf-8") as file:
    PAGE_STORE = json.load(file)

with open(INVERTED_INDEX_FILE, "r", encoding="utf-8") as file:
    INVERTED_INDEX = json.load(file)

with open(METADATA_INDEX_FILE, "r", encoding="utf-8") as file:
    METADATA_INDEX = json.load(file)

if IDF_INDEX_FILE.exists():
    with open(IDF_INDEX_FILE, "r", encoding="utf-8") as f:
        IDF_INDEX = json.load(f)
else:
    IDF_INDEX = None

STOP_WORDS = {
    "the", "is", "a", "an", "in", "on", "at", "for",
    "of", "to", "and", "or", "with", "by", "this",
    "that", "it", "as", "be", "are", "was", "were",
    "what", "how", "why", "when", "where", "who"
}

def tokenize_query(query: str):
    query = query.lower()
    query = re.sub(r"[^a-z0-9\s]", " ", query)
    tokens = query.split()
    tokens = [t for t in tokens if t not in STOP_WORDS and len(t) > 2]
    return tokens

def rbac_filter(user_role: str):
    user_role = user_role.casefold()
    return set(METADATA_INDEX.get(user_role, []))

def lexical_search(tokens, allowed_pages):
    page_scores = defaultdict(float)
    for token in tokens:
        if token not in INVERTED_INDEX:
            continue
        postings = INVERTED_INDEX[token]
        for entry in postings:
            page_id = entry["page_id"]
            tf = entry["tf"]
            if page_id not in allowed_pages:
                continue
            if IDF_INDEX:
                idf = IDF_INDEX.get(token, 1.0)
                score = tf * idf
            else:
                score = tf
            page_scores[page_id] += score
    return page_scores

def rank_pages(page_score, top_k = 5):
    ranked = sorted(page_score.items(), key = lambda x : x[1], reverse=True)
    return ranked[:top_k]

def retrieve(query: str, user_role: str, top_k: int = 5,score_threshold: float = 0.5):
    logger.info("Running lexical retrieval")

    tokens = tokenize_query(query)
    if not tokens:
        logger.warning("No valid tokens found in query")
        return []
    
    allowed_pages = rbac_filter(user_role)
    if not allowed_pages:
        logger.warning("No pages allowed for this role")
        return []
    
    page_scores = lexical_search(tokens, allowed_pages)
    if not page_scores:
        logger.info("No lexical matches found")
        return []

    ranked_pages = rank_pages(page_scores, top_k)
    filtered_pages = [(page_id, score) for page_id, score in ranked_pages if score >= score_threshold]
    contexts = []

    for page_id, score in filtered_pages:
        page_data = PAGE_STORE.get(page_id)
        if page_data:
            contexts.append({
                "page_id": page_id,
                "score": score,
                "title": page_data.get("title"),
                "content": page_data.get("content")
            })
    
    return contexts