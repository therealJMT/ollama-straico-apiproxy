import logging
import whisper
import pathlib
from fastapi import UploadFile, Form, File
from fastapi.responses import JSONResponse
from app import app
from typing import Optional
import tempfile

from os import environ

logger = logging.getLogger(__name__)

default_transcription_model = environ.get("DEFAULT_TRANSCRIPTION_MODEL", "base")


@app.post("/v1/audio/transcriptions")
async def lm_studio_transcriptions(
    file: UploadFile = File(...), model: Optional[str] = Form(None)
):
    contents = await file.read()
    model_name = default_transcription_model
    model = whisper.load_model(model_name)
    with tempfile.TemporaryDirectory() as tmpdirname:
        file = pathlib.Path(tmpdirname) / "audio.mp3"
        with file.open("wb") as writer:
            writer.write(contents)
        result = model.transcribe(str(file))

        return JSONResponse(content={"text": result["text"]})
