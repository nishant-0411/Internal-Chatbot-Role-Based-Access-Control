import sys
sys.path.append("/Users/nishant/Resume Projects/Internal-Chatbot-RBAC")
from app.services.rag_engine import retrieve_context
docs, metas = retrieve_context("What was the overall YoY revenue increase for the entire 2024 fiscal year?", "finance")
for i, (d, m) in enumerate(zip(docs.split('\n\n'), metas)):
    print(f"--- DOC {i+1} ---")
    print(d[:200])
    print("---")
print("Total chars:", len(docs))
