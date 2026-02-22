# app/services/ingestion.py -> doing vector embeddings
import os
import uuid
import yaml
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings
from app.core.logger import logger

logger.info("Initializing embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)

logger.info("Initializing ChromaDB client...")
client = chromadb.PersistentClient(path=settings.VECTOR_STORE_PATH)

def parse_markdown(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            logger.warning(f"No YAML metadata found in {filepath}")
            return None, None

        _, yaml_block, body = content.split("---", 2)
        metadata = yaml.safe_load(yaml_block)

        return metadata, body

    except Exception as e:
        logger.error(f"Markdown parsing failed: {filepath} | {str(e)}")
        return None, None


def ingest():
    logger.info("=" * 60)
    logger.info("Starting vector ingestion...")

    try:
        client.delete_collection(settings.COLLECTION_NAME)
        logger.info("Old collection deleted.")
    except Exception:
        logger.warning("No existing collection found.")

    collection = client.get_or_create_collection( name=settings.COLLECTION_NAME)

    total_chunks = 0

    for root, dirs, files in os.walk(settings.DATA_PATH):
        for file in files:

            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)
            logger.info(f"Ingesting markdown: {filepath}")

            metadata, content = parse_markdown(filepath)

            if not metadata:
                continue

            chunks = text_splitter.split_text(content)

            for chunk in chunks:
                try:
                    embedding = embedding_model.encode(chunk).tolist()

                    roles = metadata.get("role_access", [])

                    if isinstance(roles, str):
                        roles = [r.strip() for r in roles.split(",")]

                    roles = [str(r).casefold() for r in roles]

                    def safe_value(value):
                        if value is None:
                            return ""
                        if isinstance(value, (str, int, float, bool)):
                            return value
                        return str(value)

                    enriched_metadata = {
                        "title": safe_value(metadata.get("title")),
                        "department": safe_value(metadata.get("department")),
                        "sensitivity": safe_value(metadata.get("sensitivity")),
                        "document_type": safe_value(metadata.get("document_type")),
                        "fiscal_year": safe_value(metadata.get("fiscal_year")),
                        "quarter": safe_value(metadata.get("quarter")),
                        "role_access": "|" + "|".join(roles) + "|",
                        "source_file": file
                    }

                    collection.add(
                        documents=[chunk],
                        embeddings=[embedding],
                        metadatas=[enriched_metadata],
                        ids=[str(uuid.uuid4())]
                    )

                    total_chunks += 1

                except Exception as e:
                    logger.error(f"Embedding failed: {file} | {str(e)}")
    
    print("TOTAL CHUNKS STORED:", total_chunks)

    logger.info(f"Ingestion completed. Total chunks stored: {total_chunks}")
    logger.info("=" * 60)

def get_collection():
    client = chromadb.PersistentClient(path=settings.VECTOR_STORE_PATH)
    return client.get_or_create_collection(name=settings.COLLECTION_NAME)


if __name__ == "__main__":
    ingest()
