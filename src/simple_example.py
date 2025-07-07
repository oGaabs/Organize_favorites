import os
from dotenv import load_dotenv

import llm_agent

# Carregar variáveis de ambiente
load_dotenv()
CURRENT_DIR = os.getcwd()


def simple_folder_analysis():
  """Exemplo simples de análise de pasta com OpenRouter"""
  files = os.listdir(CURRENT_DIR)
  files_list = "\n".join([f"- {file}" for file in files])

  try:
    resposta = llm_agent.call_mistral_response(
        system_prompt=llm_agent.SYSTEM_ORGANIZER_PROMPT_V1,
        user_prompt=files_list,
        model=llm_agent.MODEL_MISTRAL,
        max_tokens=800,
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
      resposta = llm_agent.call_mistral_response_user(
          user_prompt=user_input,
          model="mistralai/mistral-small-3.2-24b-instruct:free",
          max_tokens=500,
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
