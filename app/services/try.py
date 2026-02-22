from app.services.ingestion import get_collection

collection = get_collection()

results = collection.query(
    query_texts=["Q4 revenue target"],
    n_results=5,
    include=["documents", "metadatas"]
)

for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print("\n----")
    print("META:", meta)
    print("DOC:", doc[:300])