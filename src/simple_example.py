import os
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
CURRENT_DIR = os.getcwd()


# =================== CONSTANTS ===================
SYSTEM_ORGANIZER_PROMPT = "Você é um especialista em organização de arquivos."
SYSTEM_CHAT_PROMPT = (
    "Você é um assistente especializado em organização de arquivos e pastas. "
    "Responda sempre em português com sugestões práticas."
)
USER_FOLDER_ANALYSIS_PROMPT = (
    "Você é um assistente de organização de arquivos.\n"
    "Aqui estão os arquivos/pastas na pasta atual:\n\n{files_list}\n\n"
    "Por favor, sugira uma estrutura de organização melhor para estes arquivos.\n"
    "Responda em português com sugestões práticas."
)
MODEL_MISTRAL = "mistralai/mistral-small-3.2-24b-instruct:free"

# =================== IA INTERACTION ===================
def get_mistral_response(system_prompt, user_prompt, model=MODEL_MISTRAL, max_tokens=800, title="Simple Folder Organizer"):
    """Função centralizada para interação com a IA via OpenRouter."""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_TOKEN"),
    )
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://github.com/folder-organizer",
            "X-Title": title,
        },
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=max_tokens
    )
    return completion.choices[0].message.content


def simple_folder_analysis():
    """Exemplo simples de análise de pasta com OpenRouter"""
    files = os.listdir(CURRENT_DIR)
    files_list = "\n".join([f"- {file}" for file in files])

    prompt = USER_FOLDER_ANALYSIS_PROMPT.replace("{files_list}", files_list)
    try:
        resposta = get_mistral_response(
            system_prompt=SYSTEM_ORGANIZER_PROMPT,
            user_prompt=prompt,
            model=MODEL_MISTRAL,
            max_tokens=800,
            title="Simple Folder Organizer"
        )
        print("🤖 Sugestões de Organização:")
        print("=" * 40)
        print(resposta)
        print("=" * 40)
    except Exception as e:
        print(f"❌ Erro: {str(e)}")



def chat_with_organizer():
    """Chat simples com o agente organizador"""
    print("💬 Chat com Agente Organizador")
    print("Digite 'sair' para terminar")
    print("-" * 30)
    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("👋 Até logo!")
            break
        try:
            resposta = get_mistral_response(
                system_prompt=SYSTEM_CHAT_PROMPT,
                user_prompt=user_input,
                model="mistralai/mistral-small-3.2-24b-instruct:free",
                max_tokens=500,
                title="Folder Organizer Chat"
            )
            print(f"\n🤖 Agente: {resposta}")
        except Exception as e:
            print(f"❌ Erro: {str(e)}")


if __name__ == "__main__":
    print("🚀 Agente Organizador de Pastas - Exemplo Simples")
    print("\nEscolha uma opção:")
    print("1. Analisar pasta atual")
    print("2. Chat com agente")

    choice = input("\nOpção (1 ou 2): ").strip()

    if choice == "1":
        simple_folder_analysis()
    elif choice == "2":
        chat_with_organizer()
    else:
        print("❌ Opção inválida")
