# Desafio Técnico para Desenvolvedor Cognitiva Brasil

Este repositório contém a solução para o desafio técnico proposto pela Cognitiva Brasil. O objetivo é desenvolver uma solução que acesse três plataformas de Modelos de Linguagem de Grande Escala (LLMs) diferentes, gere respostas para uma mesma pergunta e realize uma análise comparativa da qualidade das respostas.

## Requisitos do Desafio

1. **Acesso a Três LLMs Diferentes**:
   - Foram utilizados os seguintes modelos:
     - **Google Gemini**
     - **Qwen**
     - **Llama**

2. **Envio de uma Mesma Pergunta**:
   - Uma pergunta é enviada para cada modelo, e as respostas são capturadas.

3. **Mecanismo de Comparação**:
   - As respostas são comparadas com base nos seguintes critérios:
     - Clareza e coerência da resposta
     - Precisão da informação
     - Criatividade ou profundidade da resposta
     - Consistência gramatical

4. **Autoavaliação Assistida por IA**:
   - As respostas são devolvidas aos próprios modelos para que eles ranqueiem as melhores respostas.

## Como Executar o Código

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Acesso às APIs dos modelos utilizados (Google Gemini, Qwen, Llama). Certifique-se de ter as chaves de API necessárias.

### Passos para Execução

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/pauloandrepassos/desafio-cognitiva
   cd desafio-cognitiva
   ```

2. **Instale as Dependências**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as Chaves de API**:

   - Renomeie o arquivo `.env.example` para `.env`:

     ```bash
     cp .env.example .env
     ```
   - Edite o arquivo `.env` e adicione as chaves API para os modelos utilizados. Exemplo:

     ```plaintext
     GEMINI_API_KEY=sua_chave_aqui
     OPENROUTER_API_KEY=sua_chave_aqui
     ```
     Nota: O Open Router é usado para acessar os modelos Qwen e Llama. A chave do Open Router deve ser configurada no campo `OPENROUTER_API_KEY`.

5. **Execute o Código**:

   ```bash
   python main.py
   ```

   O código enviará a pergunta para os modelos, capturará as respostas, realizará a comparação e exibirá o modelo com a melhor resposta.

### Exemplo de Saída

Ao executar o código, você verá uma saída semelhante a esta:

```
Pergunta: Quais são as fases da Lua?

--- Respostas dos Modelos ---
🔹 Gemini: As fases da Lua são...
🔹 Qwen: As fases da Lua incluem...
🔹 Llama: A Lua passa por várias fases...

--- Rankings dos Modelos ---
🔹 Ranking do Gemini: [1, 2, 3]
🔹 Ranking do Qwen: [2, 3, 1]
🔹 Ranking do Llama: [3, 1, 2]

🏆 Modelo com a melhor resposta: Gemini
```
