import json
import requests
from app.core.config import settings
from app.core.logger import logger

def stream_ollama(prompt: str):
    try:
        response = requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": True,
                "options": {
                    "num_ctx": 8192
                }
            },
            stream=True,
            timeout=120
        )

        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                yield data.get("response", "")

    except Exception as e:
        logger.error(f"Streaming error: {str(e)}")
        yield "Error generating response."