from google import genai
from google.genai import types
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Header
import os
from pydantic import BaseModel

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

API_KEY_CREDITS = {os.getenv("APP_API_KEY"): 10} # a dictionary to tell how many credits are set to a single API Key

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits left")
    return x_api_key

@app.post("/generate")
def generate(request: PromptRequest, x_api_key = Depends(verify_api_key)):
    prompt = request.prompt
    API_KEY_CREDITS[x_api_key] -= 1
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are Google's customer service agent. Answer customer's questions politely."),
        contents=prompt
    )
    return response.text