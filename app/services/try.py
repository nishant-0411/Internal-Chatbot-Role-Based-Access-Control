import chromadb

COLLECTION_NAME = "internal_docs"

client = chromadb.PersistentClient(path = "./vector_db")
collection = client.get_or_create_collection(name=COLLECTION_NAME)

results = collection.query(
    query_texts=["What is the system architecture?"],
    where={"allowed_roles": {"$contains": "marketing"}},
    n_results=3
)

print(results["documents"])