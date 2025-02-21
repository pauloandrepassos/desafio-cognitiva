import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def perguntar_ao_gemini(pergunta):
    resposta = model.generate_content(pergunta)
    return resposta.text
