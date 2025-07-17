from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.detect import detect_language

app = FastAPI()

class TextInput(BaseModel):
    text: str = 'Bonjour le monde'

@app.post("/detect")
def detect(input: TextInput):
    try:
        return detect_language(input.text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
