import requests
from dotenv import load_dotenv
import os

load_dotenv()

payload = {'prompt': "What is Google's privacy policy? I'm afraid of my data leaking.."}
url = "http://127.0.0.1:8000/generate"
headers = {"x-api-key": os.getenv("APP_API_KEY"), "Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())