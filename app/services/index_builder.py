#Data parsing and Index building for tree generation
import os
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict, Counter
from app.core.config import settings
from app.core.logger import logger

INDEX_PATH = Path("page_index")
PAGE_STORE_FILE = INDEX_PATH / "page_store.json"
INVERTED_INDEX_FILE = INDEX_PATH / "inverted_index.json"
METADATA_INDEX_FILE = INDEX_PATH / "metadata_index.json"
IDF_INDEX_FILE = INDEX_PATH / "idf_index.json"
STOP_WORDS = {
        "the","is","a","an","in","on","at","for",
        "of","to","and","or","with","by","this",
        "that","it","as","be","are","was","were",
        "what", "how", "why", "when", "where", "who"
    }

class IndexBuilder:
    def __init__(self):
        self.page_store = {}
        self.inverted_index = defaultdict(list)
        self.metadata_index = defaultdict(list)

    def build(self):
        logger.info("=" * 60)
        logger.info("Starting PageIndex build process...")

        INDEX_PATH.mkdir(exist_ok=True)
        total_pages = 0

        for root, _, files in os.walk(settings.DATA_PATH):
            for file in files:
                if not file.endswith("md"):
                    continue

                filepath = Path(root)/file
                logger.info(f"Processing: {filepath}")

                metadata, body = self.parse_markdown(filepath)

                if not metadata:
                    continue
                
                sections = self.split_into_sections(body)

                for idx, section in enumerate(sections):
                    page_id = self.generate_page_id(filepath, idx)

                    roles = metadata.get("role_access", [])
                    if isinstance(roles, str):
                        roles = [r.strip().casefold() for r in roles.split(",")]
                    else:
                        roles = [str(r).casefold() for r in roles]

                    page_data = {
                        "title": metadata.get("title"),
                        "department": metadata.get("department"),
                        "sensitivity": metadata.get("sensitivity"),
                        "document_type": metadata.get("document_type"),
                        "last_updated": str(metadata.get("last_updated")) if metadata.get("last_updated") else None,
                        "version": metadata.get("version"),
                        "role_access": roles,
                        "source_file": file,
                        "content": section.strip()
                    }

                    self.page_store[page_id] = page_data
                    self.index_content(page_id, section)

                    for role in roles:
                        self.metadata_index[role].append(page_id)
                    total_pages += 1
        
        self.write_indexes()

        logger.info(f"PageIndex build completed. Total sections indexed: {total_pages}")
        logger.info("=" * 60)

    def parse_markdown(self, filepath):
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

    def split_into_sections(self, body):
        sections = re.split(r"\n##+\s+", body)
        return [sec.strip() for sec in sections if sec.strip()]

    def tokenize(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        tokens = text.split()
        tokens = [t for t in tokens if t not in STOP_WORDS and len(t) > 2]
        return tokens

    def index_content(self, page_id, content):
        tokens = self.tokenize(content)
        token_counts = Counter(tokens)
        for token, count in token_counts.items():
            self.inverted_index[token].append({"page_id": page_id,"tf": count})
    
    def generate_page_id(self, filepath, section_index):
        relative_path = Path(filepath).relative_to(settings.DATA_PATH)
        base = str(relative_path).replace("/", "_").replace(".md", "")
        return f"{base}_sec_{section_index}"
    
    def write_indexes(self):
        with open(PAGE_STORE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.page_store, f, indent=2)
        with open(INVERTED_INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(dict(self.inverted_index), f, indent=2)
        with open(METADATA_INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(dict(self.metadata_index), f, indent=2)

        import math
        idf_index = {}
        total_docs = len(self.page_store)
        if total_docs > 0:
            for token, postings in self.inverted_index.items():
                doc_freq = len(postings)
                idf_index[token] = math.log(total_docs / (1 + doc_freq)) + 1.0

        with open(IDF_INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(idf_index, f, indent=2)

if __name__ == "__main__":
    builder = IndexBuilder()
    builder.build()