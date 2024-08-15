import json
import logging

from fastapi import Request
from fastapi.responses import StreamingResponse
from app import app

import io
from os import environ

logger = logging.getLogger(__name__)

default_embedding_model = environ.get(
    "DEFAULT_EMBEDDING_MODEL", "nomic-ai/nomic-embed-text-v1.5"
)


@app.post("/v1/audio/speech")
async def lm_studio_tts(request: Request):
    try:
        post_json_data = await request.json()
    except:
        post_json_data = json.loads((await request.body()).decode())
    logger.debug(post_json_data)

    model = post_json_data["model"]
    input_text = post_json_data["input"]
    voice = post_json_data["voice"]

    sample_path = "/Users/jr/Documents/audio/How can we even hear gravitational waves.mp3"
    with open(sample_path, "rb") as reader:
        data = reader.read(-1)
        stream = io.BytesIO(data)
        return StreamingResponse(stream, media_type="application/octet-stream")