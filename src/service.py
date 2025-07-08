from pydantic import BaseModel
from openai import OpenAI
from pydantic import Field
from dotenv import load_dotenv
load_dotenv()

class WordLevel(BaseModel):
    word: str = Field(..., description="Individual word in the given text to be checked CEFR level")
    level: str = Field(..., description="CEFR level of the word, e.g., A1, A2, B1, B2, C1, C2")

class WordLevelResponse(BaseModel):
    results: list[WordLevel] = Field(..., description="List of words with their CEFR levels")


def check_word_levels(text: str) -> WordLevelResponse:
    client = OpenAI()

    completion = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Your duty is to check every word in the given text and provide its CEFR level. Don't skip any word, even if it is a common word."},
            {"role": "user", "content": f"Given text: {text} \nPlease provide the CEFR level for each word in the text."},
        ],
        response_format=WordLevelResponse,
    )

    result = completion.choices[0].message.parsed
    return result