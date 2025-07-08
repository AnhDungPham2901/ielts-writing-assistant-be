# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import service
from loguru import logger

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/word-level-check")
def check_word_levels(request: TextRequest) -> dict:
    """
    Check the CEFR levels of each word in the given text.
    """
    result = service.check_word_levels(request.text)
    if not result:
        logger.error("No words found or unable to process the text.")
        return {"error": "No words found or unable to process the text."}
    logger.info(f"Number of words checked: {len(result.results)}")
    # Convert the result to a dictionary format
    word_levels = {word.word: word.level for word in result.results}
    return word_levels