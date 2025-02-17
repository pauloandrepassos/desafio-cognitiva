from gemini import perguntar_ao_gemini
from mistral import perguntar_ao_mistral
from llama import perguntar_ao_llama
import re

def rankear_respostas(pergunta, respostas):
    prompt = f"Pergunta: {pergunta}\n\n"
    prompt += "Aqui estão as três respostas para a pergunta. Classifique-as da melhor para a pior:\n\n"
    
    for idx, resposta in enumerate(respostas, 1):
        prompt += f"Resposta {idx}: {resposta}\n"
    
    prompt += "\nPor favor, retorne o ranking apenas no formato: [1, 2, 3]."
    ranking_gemini = perguntar_ao_gemini(prompt)
    ranking_mistral = perguntar_ao_mistral(prompt)
    ranking_llama = perguntar_ao_llama(prompt)
    
    def extrair_ranking(resposta):
        match = re.search(r'\[\d,\s\d,\s\d\]', resposta)
        if match:
            return match.group(0)
        else:
            return "Erro: Ranking não encontrado"
    
    ranking_gemini = extrair_ranking(ranking_gemini)
    ranking_mistral = extrair_ranking(ranking_mistral)
    ranking_llama = extrair_ranking(ranking_llama)
    
    return ranking_gemini, ranking_mistral, ranking_llama

def determinar_modelo_vencedor(ranking_gemini, ranking_mistral, ranking_llama):
    def contar_posicoes(ranking):
        ranking = eval(ranking)
        posicoes = {"Gemini": 0, "Mistral": 0, "Llama": 0}
        posicoes["Gemini"] = ranking.index(1) + 1
        posicoes["Mistral"] = ranking.index(2) + 1
        posicoes["Llama"] = ranking.index(3) + 1
        return posicoes

    posicoes_gemini = contar_posicoes(ranking_gemini)
    posicoes_mistral = contar_posicoes(ranking_mistral)
    posicoes_llama = contar_posicoes(ranking_llama)

    melhores_posicoes = {
        "Gemini": posicoes_gemini["Gemini"],
        "Mistral": posicoes_mistral["Mistral"],
        "Llama": posicoes_llama["Llama"]
    }

    modelo_vencedor = min(melhores_posicoes, key=melhores_posicoes.get)
    return modelo_vencedor

pergunta = "Quem é a pessoa mais rica do mundo?"
resposta_gemini = perguntar_ao_gemini(pergunta)
resposta_mistral = perguntar_ao_mistral(pergunta)
resposta_llama = perguntar_ao_llama(pergunta)

print("\n--- Respostas dos Modelos ---")
print(f"🔹 Gemini: {resposta_gemini}")
print("\n----------------")
print(f"🔹 Mistral: {resposta_mistral}")
print("\n----------------")
print(f"🔹 Llama: {resposta_llama}")
print("\n----------------")

respostas = [resposta_gemini, resposta_mistral, resposta_llama]
ranking_gemini, ranking_mistral, ranking_llama = rankear_respostas(pergunta, respostas)

print("\n--- Rankings dos Modelos ---")
print(f"🔹 Ranking do Gemini: {ranking_gemini}")
print("\n----------------")
print(f"🔹 Ranking do Mistral: {ranking_mistral}")
print("\n----------------")
print(f"🔹 Ranking do Llama: {ranking_llama}")
print("\n----------------")

modelo_vencedor = determinar_modelo_vencedor(ranking_gemini, ranking_mistral, ranking_llama)
print(f"\n🏆 Modelo com a melhor resposta: {modelo_vencedor}")