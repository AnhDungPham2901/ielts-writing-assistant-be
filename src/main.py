# main.py
from fastapi import FastAPI
import service

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/task-completion-check")
def check_task_completion(task: str, response: str):
    """
    Check if the task is completed based on the response.
    """
    result = service.check_task_completion(task, response)
    return result