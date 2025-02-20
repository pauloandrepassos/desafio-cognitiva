import re
from gemini import perguntar_ao_gemini
from llama import perguntar_ao_llama
from qwen import perguntar_ao_qwen

import re

def rankear_respostas(pergunta, respostas):
    def extrair_ranking(resposta):
        match = re.search(r'\[(\d),\s*(\d),\s*(\d)\]', resposta)
        if match:
            ranking = [int(match.group(1)), int(match.group(2)), int(match.group(3))]
            if sorted(ranking) == [1, 2, 3]:
                return f"[{ranking[0]}, {ranking[1]}, {ranking[2]}]"
        return None

    while True:
        prompt = f"Pergunta: {pergunta}\n\n"
        prompt += "Aqui estão as três respostas para a pergunta. Classifique-as da melhor para a pior com base nos seguintes critérios:\n\n"
        prompt += "1. Clareza e coerência da resposta: A resposta é fácil de entender e está logicamente organizada?\n"
        prompt += "2. Precisão da informação: A resposta é factualmente correta e relevante para a pergunta?\n"
        prompt += "3. Criatividade ou profundidade da resposta: A resposta traz insights originais ou uma análise aprofundada?\n"
        prompt += "4. Consistência gramatical: A resposta está bem escrita, sem erros gramaticais ou ortográficos?\n\n"
        
        for idx, resposta in enumerate(respostas, 1):
            prompt += f"Resposta {idx}: {resposta}\n"
        
        prompt += "\nPor favor, retorne o ranking apenas no formato: [1, 2, 3], considerando 1 a melhor resposta e 3 a pior.\n"
        prompt += "Exemplo de saída esperada: [1, 2, 3]\n"
        prompt += "Lembre-se: o ranking deve ser exatamente no formato [1, 2, 3], sem texto adicional."
        
        ranking_gemini = perguntar_ao_gemini(prompt)
        ranking_qwen = perguntar_ao_qwen(prompt)
        ranking_llama = perguntar_ao_llama(prompt)
        
        ranking_gemini = extrair_ranking(ranking_gemini)
        ranking_qwen = extrair_ranking(ranking_qwen)
        ranking_llama = extrair_ranking(ranking_llama)
        
        if ranking_gemini and ranking_qwen and ranking_llama:
            break
        else:
            print("Erro ao extrair o ranking. Tentando novamente...")

    return ranking_gemini, ranking_qwen, ranking_llama

def determinar_modelo_vencedor(ranking_gemini, ranking_qwen, ranking_llama):
    def obter_primeira_e_segunda_posicao(ranking):
        ranking = eval(ranking)
        return ranking[0], ranking[1]

    primeira_posicao_gemini, segunda_posicao_gemini = obter_primeira_e_segunda_posicao(ranking_gemini)
    primeira_posicao_qwen, segunda_posicao_qwen = obter_primeira_e_segunda_posicao(ranking_qwen)
    primeira_posicao_llama, segunda_posicao_llama = obter_primeira_e_segunda_posicao(ranking_llama)

    if primeira_posicao_gemini == primeira_posicao_qwen:
        return primeira_posicao_gemini
    elif primeira_posicao_gemini == primeira_posicao_llama:
        return primeira_posicao_gemini
    elif primeira_posicao_qwen == primeira_posicao_llama:
        return primeira_posicao_qwen
    elif segunda_posicao_gemini == segunda_posicao_qwen:
        return segunda_posicao_gemini
    elif segunda_posicao_gemini == segunda_posicao_llama:
        return segunda_posicao_gemini
    elif segunda_posicao_qwen == segunda_posicao_llama:
        return segunda_posicao_qwen
    else:
        return "Empate entre todos os modelos"


pergunta = "Quais são as fases da Lua?"
print(f"Pergunta: {pergunta}\n")
resposta_gemini = perguntar_ao_gemini(pergunta)
resposta_qwen = perguntar_ao_qwen(pergunta)
resposta_llama = perguntar_ao_llama(pergunta)

print("\n--- Respostas dos Modelos ---")
print(f"🔹 Gemini: {resposta_gemini}")
print("\n----------------")
print(f"🔹 qwen: {resposta_qwen}")
print("\n----------------")
print(f"🔹 Llama: {resposta_llama}")
print("\n----------------")

respostas = [resposta_gemini, resposta_qwen, resposta_llama]
ranking_gemini, ranking_qwen, ranking_llama = rankear_respostas(pergunta, respostas)

print("\n--- Rankings dos Modelos ---")
print(f"🔹 Ranking do Gemini: {ranking_gemini}")
print("\n----------------")
print(f"🔹 Ranking do qwen: {ranking_qwen}")
print("\n----------------")
print(f"🔹 Ranking do Llama: {ranking_llama}")
print("\n----------------")

modelo_vencedor = determinar_modelo_vencedor(ranking_gemini, ranking_qwen, ranking_llama)
print(f"\n🏆 Modelo com a melhor resposta: {modelo_vencedor}")