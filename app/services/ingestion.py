# Make the raw data into AI readable form i.e into vectors 

import os 
import uuid
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter 

data_path = "./data"
store_path = "./vector_db"
COLLECTION_NAME = "internal_docs"

role_folder_mapping = {
    # department : who can access
    "hr": ["hr", "c-level"],
    "finance": ["finance", "c-level"],
    "marketing": ["marketing", "c-level"],
    "engineering": ["engineering", "c-level"],
    "general": ["employee", "finance", "marketing", "hr", "engineering", "c-level"]
}

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
text_splitters = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
client = chromadb.PersistentClient(path = store_path)

try :
    client.delete_collection(COLLECTION_NAME)
except:
    pass

collection = client.get_or_create_collection(name=COLLECTION_NAME)

def read_files(filepath):
    try:
        if filepath.endswith(".md"):
            with open(filepath,'r',encoding="utf-8") as file:
                return file.read()
        elif filepath.endswith(".csv"):
            df = pd.read_csv(filepath)
            return df.to_string()
        
    except Exception as e:
        print(f"error reading the {filepath}: {e}")

    return None

def ingest():
    for folder in os.listdir(data_path):

        folder_path = os.path.join(data_path, folder)

        if folder.startswith('.') or not os.path.isdir(folder_path):
            continue

        department = folder.casefold()

        if department not in role_folder_mapping:
            print(f"No role mapping for {department}, skipping....")
            continue

        allowed_roles = role_folder_mapping[department]

        for file in os.listdir(folder_path):

            if not(file.endswith(".md") or file.endswith(".csv")):
                continue
            
            filepath = os.path.join(folder_path, file)

            content = read_files(filepath)

            if not content:
                continue

            chunks = text_splitters.split_text(content)

            for chunk in chunks:
                embedding = embedding_model.encode(chunk).tolist()

                metadata = {
                    "department": department,
                    "file": file,
                    "allowed_roles": allowed_roles
                }

                collection.add(
                    metadatas = [metadata],
                    embeddings = [embedding],
                    documents= [chunk],
                    ids = [str(uuid.uuid4())]
                )


if __name__ == "__main__":
    ingest()
        
        
