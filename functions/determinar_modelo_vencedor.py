def determinar_modelo_vencedor(ranking_gemini, ranking_qwen, ranking_llama):
    modelos = {
        1: "Gemini",
        2: "Qwen",
        3: "Llama"
    }

    def obter_primeira_e_segunda_posicao(ranking):
        ranking = eval(ranking)
        return ranking[0], ranking[1]

    primeira_posicao_gemini, segunda_posicao_gemini = obter_primeira_e_segunda_posicao(ranking_gemini)
    primeira_posicao_qwen, segunda_posicao_qwen = obter_primeira_e_segunda_posicao(ranking_qwen)
    primeira_posicao_llama, segunda_posicao_llama = obter_primeira_e_segunda_posicao(ranking_llama)

    if primeira_posicao_gemini == primeira_posicao_qwen:
        return modelos[primeira_posicao_gemini]
    elif primeira_posicao_gemini == primeira_posicao_llama:
        return modelos[primeira_posicao_gemini]
    elif primeira_posicao_qwen == primeira_posicao_llama:
        return modelos[primeira_posicao_qwen]
    elif segunda_posicao_gemini == segunda_posicao_qwen:
        return modelos[segunda_posicao_gemini]
    elif segunda_posicao_gemini == segunda_posicao_llama:
        return modelos[segunda_posicao_gemini]
    elif segunda_posicao_qwen == segunda_posicao_llama:
        return modelos[segunda_posicao_qwen]

    else:
        return "Empate entre todos os modelos"