import sys
sys.path.append("/Users/nishant/Resume Projects/Internal-Chatbot-RBAC")
from app.services.rag_engine import retrieve_context
c, s = retrieve_context("What was the Q4 revenue target?", "finance")
print("RESULT context length:", len(c))
print("RESULT sources count:", len(s))
