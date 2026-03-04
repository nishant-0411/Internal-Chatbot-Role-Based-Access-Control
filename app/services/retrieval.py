import re
from rank_bm25 import BM25Okapi
from app.services.index_builder import CHUNKS
from app.core.logger import logger

BM25_INDEX = None
TOKENIZED_CORPUS = []
CHUNK_REFERENCES = []

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
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 2]

def initialize_bm25():
    global BM25_INDEX, TOKENIZED_CORPUS, CHUNK_REFERENCES
    
    logger.info("Initializing BM25 Index...")
    TOKENIZED_CORPUS.clear()
    CHUNK_REFERENCES.clear()

    for chunk in CHUNKS:
        CHUNK_REFERENCES.append(chunk)
        tokens = tokenize_query(chunk["content"])
        TOKENIZED_CORPUS.append(tokens)

    if TOKENIZED_CORPUS:
        BM25_INDEX = BM25Okapi(TOKENIZED_CORPUS)
    logger.info("BM25 Index initialized successfully.")

def retrieve(query: str, user_role: str, top_k: int = 3):
    logger.info("Running BM25 retrieval")
    
    if not BM25_INDEX:
        logger.warning("BM25 index not initialized.")
        return []

    tokens = tokenize_query(query)
    if not tokens:
        logger.warning("No valid tokens found in query")
        return []

    scores = BM25_INDEX.get_scores(tokens)
    user_role = user_role.casefold()

    import heapq
    scored_chunks = []
    
    for idx, score in enumerate(scores):
        if score <= 0:
            continue
            
        chunk = CHUNK_REFERENCES[idx]
        roles = chunk.get("role_access")
        
        if not roles or user_role in roles:
            scored_chunks.append((score, chunk))

    top_scored_chunks = heapq.nlargest(top_k, scored_chunks, key=lambda x: x[0])
    
    contexts = []
    for score, chunk in top_scored_chunks:
        contexts.append({
            "score": score,
            "title": chunk.get("document_name", "Unknown Document"),
            "section": chunk.get("section_title", "Unknown Section"),
            "content": chunk.get("content", "")
        })
    
    return contexts