from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
import requests

app = FastAPI(title="AI Product Manager Assistant API")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("Please set the GEMINI_API_KEY environment variable")

GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

class FeaturesRequest(BaseModel):
    features: str  # Multiline string input with product features/backlog items

class FeaturesResponse(BaseModel):
    insights: str

def call_gemini_api(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(GEMINI_ENDPOINT, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"GEMINI API Error: {response.text}")
    data = response.json()
    return data['candidates'][0]['content']['parts'][0]['text']

@app.post("/analyze-features", response_model=FeaturesResponse)
def analyze_features(req: FeaturesRequest):
    prompt = f"""You are an AI Product Manager assistant. Analyze the following product backlog items and provide:
- Prioritized key features
- Potential risks
- Suggestions for improvement

Backlog Items:
\"\"\"{req.features}\"\"\"
Response:"""

    insights = call_gemini_api(prompt)
    return FeaturesResponse(insights=insights)
