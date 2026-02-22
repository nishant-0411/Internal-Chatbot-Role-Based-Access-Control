import redis
import json
from app.core.logger import logger
from app.core.config import settings

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
MAX_HISTORY = settings.MAX_HISTORY

try:
    redis_client.ping()
    logger.info("Redis connected successfully.")
except Exception as e:
    logger.error(f"Redis connection failed: {str(e)}")

def add_message(username: str, conversation_id: str, role: str, content: str):
    key = f"chat:{username}:{conversation_id}"

    message = json.dumps({"role": role,"content": content})

    redis_client.rpush(key, message)
    redis_client.ltrim(key, -MAX_HISTORY, -1)

def get_messages(username: str, conversation_id: str):
    key = f"chat:{username}:{conversation_id}"
    messages = redis_client.lrange(key, 0, -1)
    return [json.loads(msg) for msg in messages]

def delete_conversation(username: str, conversation_id: str):
    key = f"chat:{username}:{conversation_id}"
    redis_client.delete(key)