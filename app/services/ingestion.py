# Make the raw data into AI readable form i.e into vectors 

import os 
import uuid
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from app.core.config import settings
from app.core.logger import logger

data_path = "./data"
store_path = "./vector_db"

role_folder_mapping = {
    # department : who can access
    "hr": ["hr", "c-level"],
    "finance": ["finance", "c-level"],
    "marketing": ["marketing", "c-level"],
    "engineering": ["engineering", "c-level"],
    "general": ["employee", "finance", "marketing", "hr", "engineering", "c-level"]
}

logger.info("Initializing embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

text_splitters = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

logger.info("Initializing ChromaDB client...")
client = chromadb.PersistentClient(path = store_path)

collection = client.get_or_create_collection(name=settings.COLLECTION_NAME)
logger.info(f"Connected to collection: {settings.COLLECTION_NAME}")

def read_files(filepath):
    try:
        if filepath.endswith(".md"):
            with open(filepath,'r',encoding="utf-8") as file:
                return file.read()
        elif filepath.endswith(".csv"):
            df = pd.read_csv(filepath)
            return df.to_string()
        
    except Exception as e:
        logger.error(f"Error reading file {filepath}: {str(e)}")

    return None

def ingest():
    logger.info("Starting ingestion process...")
    try:
        client.delete_collection(settings.COLLECTION_NAME)
        logger.info("Existing collection deleted successfully.")
    except Exception:
        logger.warning("No existing collection found or deletion skipped.")
    
    global collection
    collection = client.get_or_create_collection(name=settings.COLLECTION_NAME)
    logger.info("New collection initialized.")

    total_files = 0
    total_chunks = 0

    for folder in os.listdir(data_path):

        folder_path = os.path.join(data_path, folder)

        if folder.startswith('.') or not os.path.isdir(folder_path):
            continue

        department = folder.casefold()

        if department not in role_folder_mapping:
            logger.warning(f"No role mapping found for department: {department}. Skipping.")
            continue
        
        logger.info(f"Processing department: {department}")
        allowed_roles = role_folder_mapping[department]

        for file in os.listdir(folder_path):

            if not(file.endswith(".md") or file.endswith(".csv")):
                continue
            
            filepath = os.path.join(folder_path, file)
            logger.info(f"Ingesting file: {filepath}")

            content = read_files(filepath)

            if not content:
                logger.warning(f"No content extracted from {filepath}. Skipping.")
                continue

            chunks = text_splitters.split_text(content)
            logger.info(f"File split into {len(chunks)} chunks.")

            total_files += 1
            total_chunks += len(chunks)

            for chunk in chunks:
                try:
                    embedding = embedding_model.encode(chunk).tolist()

                    metadata = {
                        "department": department,
                        "file": file,
                        "allowed_roles": allowed_roles
                    }

                    collection.add(
                        metadatas=[metadata],
                        embeddings=[embedding],
                        documents=[chunk],
                        ids=[str(uuid.uuid4())]
                    )

                except Exception as e:
                    logger.error(f"Embedding failed for chunk in {file}: {str(e)}")

    logger.info("Ingestion completed successfully.")
    logger.info(f"Total files processed: {total_files}")
    logger.info(f"Total chunks stored: {total_chunks}")
    logger.info("-" * 60)


if __name__ == "__main__":
    ingest()
        
        
