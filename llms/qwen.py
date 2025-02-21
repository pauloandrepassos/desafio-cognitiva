import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def perguntar_ao_qwen(pergunta):
    payload = {
        "model": "qwen/qwen-vl-plus:free",
        "messages": [{"role": "user", "content": pergunta}],
        "max_tokens": 500
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    else:
        return f"Erro: {response.status_code} - {response.text}"
