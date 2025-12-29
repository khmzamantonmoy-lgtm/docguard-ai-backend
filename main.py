from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class DocumentRequest(BaseModel):
    document_text: str

@app.post("/analyze")
def analyze_document(request: DocumentRequest):
    prompt = f"""
You are a legal document review assistant.
Summarize the document below in simple language.

Document:
{request.document_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return {"result": response.choices[0].message.content}

