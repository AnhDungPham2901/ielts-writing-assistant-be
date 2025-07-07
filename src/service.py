from pydantic import BaseModel
from openai import OpenAI

class CheckResult(BaseModel):
    task_name: str
    is_passed: str
    description: str

class TaskCheckResponses(BaseModel):
    results: list[CheckResult]


def check_task_completion(task: str, response: str) -> TaskCheckResponses:
    client = OpenAI()
    completion = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
        ],
        response_format=TaskCheckResponses,
    )

    result = completion.choices[0].message.parsed
    return result