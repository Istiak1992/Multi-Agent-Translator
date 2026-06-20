from fastapi import FastAPI

from app.schemas.request import (
    TranslationRequest
)

from app.services.orchestrator import (
    MultiAgentTranslator
)

app = FastAPI()

translator = MultiAgentTranslator()


@app.get("/")
def home():

    return {
        "message":
        "Multi-Agent Translator Running"
    }


@app.post("/translate")
def translate(
    request: TranslationRequest
):

    return translator.execute(
        request.text,
        request.source_lang,
        request.target_lang
    )