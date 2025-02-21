import re

def extrair_ranking(resposta):
    match = re.search(r'\[(\d),\s*(\d),\s*(\d)\]', resposta)
    if match:
        ranking = [int(match.group(1)), int(match.group(2)), int(match.group(3))]
        if sorted(ranking) == [1, 2, 3]:
            return f"[{ranking[0]}, {ranking[1]}, {ranking[2]}]"
    return None