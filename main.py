from functions.rankear_respostas import rankear_respostas
from functions.determinar_modelo_vencedor import determinar_modelo_vencedor
from llms.gemini import perguntar_ao_gemini
from llms.llama import perguntar_ao_llama
from llms.qwen import perguntar_ao_qwen

def main():
    pergunta = "Qual o maior planeta do sistema solar?"
    print(f"Pergunta: {pergunta}\n")
    
    resposta_gemini = perguntar_ao_gemini(pergunta)
    resposta_qwen = perguntar_ao_qwen(pergunta)
    resposta_llama = perguntar_ao_llama(pergunta)

    print("\n--- Respostas dos Modelos ---")
    print(f"🔹 Gemini: {resposta_gemini}")
    print("\n----------------")
    print(f"🔹 Qwen: {resposta_qwen}")
    print("\n----------------")
    print(f"🔹 Llama: {resposta_llama}")
    print("\n----------------")

    respostas = [resposta_gemini, resposta_qwen, resposta_llama]
    ranking_gemini, ranking_qwen, ranking_llama = rankear_respostas(pergunta, respostas)

    print("\n--- Rankings dos Modelos ---")
    print(f"🔹 Ranking do Gemini: {ranking_gemini}")
    print("\n----------------")
    print(f"🔹 Ranking do Qwen: {ranking_qwen}")
    print("\n----------------")
    print(f"🔹 Ranking do Llama: {ranking_llama}")
    print("\n----------------")

    modelo_vencedor = determinar_modelo_vencedor(ranking_gemini, ranking_qwen, ranking_llama)
    print(f"\n🏆 Modelo com a melhor resposta: {modelo_vencedor}")

if __name__ == "__main__":
    main()