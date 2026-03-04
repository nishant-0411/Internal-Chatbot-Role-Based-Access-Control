import os
import re
import yaml
from pathlib import Path
from app.core.config import settings
from app.core.logger import logger

CHUNKS = []

class IndexBuilder:
    def __init__(self):
        pass

    def build(self):
        global CHUNKS
        CHUNKS.clear()
        
        logger.info("=" * 60)
        logger.info("Starting in-memory BM25 chunk build process...")

        total_chunks = 0
        total_pages = 0

        for root, _, files in os.walk(settings.DATA_PATH):
            for file in files:
                if not file.endswith(".md"):
                    continue

                filepath = Path(root) / file
                logger.info(f"Processing: {filepath}")

                metadata, body = self.parse_markdown(filepath)

                if not metadata:
                    continue
                
                sections = self.split_into_sections(body)

                roles = metadata.get("role_access", [])
                if isinstance(roles, str):
                    roles = set(r.strip().casefold() for r in roles.split(","))
                elif roles:
                    roles = set(str(r).casefold() for r in roles)
                else:
                    roles = set()

                for section in sections:
                    if not section.strip():
                        continue
                    
                    words = section.strip().split()
                    if not words:
                        continue
                        
                    chunk_size = 150
                    overlap = 30
                    step = chunk_size - overlap
                    
                    for i in range(0, len(words), step):
                        chunk_text = " ".join(words[i : i + chunk_size])
                        
                        CHUNKS.append({
                            "document_name": metadata.get("title", file),
                            "section_title": metadata.get("document_type", "General"),
                            "department": metadata.get("department", "General"),
                            "sensitivity": metadata.get("sensitivity", "Internal"),
                            "role_access": roles,
                            "content": chunk_text
                        })
                        total_chunks += 1
                total_pages += 1
        
        logger.info(f"PageIndex build completed. Total documents: {total_pages}, Total chunks: {total_chunks}")
        logger.info("=" * 60)

    def parse_markdown(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.startswith("---"):
                logger.warning(f"No YAML metadata found in {filepath}")
                return None, None

            parts = content.split("---", 2)
            if len(parts) < 3:
                return None, None
                
            metadata = yaml.safe_load(parts[1])
            return metadata, parts[2]

        except Exception as e:
            logger.error(f"Markdown parsing failed: {filepath} | {str(e)}")
            return None, None

    def split_into_sections(self, body):
        sections = re.split(r"\n##+\s+", body)
        return [sec.strip() for sec in sections if sec.strip()]

def build_index():
    builder = IndexBuilder()
    builder.build()