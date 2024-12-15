from src.agents.entrada.entrada_agent import EntradaAgent
from src.agents.motor.motor_agent import MotorAgent

entrada_agent = EntradaAgent()
motor_agent = MotorAgent()

print("Digite 'sair' para encerrar a conversa.")
while True:
    user_input = input("Oficio: ")
    if user_input.lower() == "sair":
        print("Agente: Até mais!")
        break

    # Obter a resposta do LLM
    interpretacao = entrada_agent.interpretar(user_input)
    
    print(f"Agente: {interpretacao}")
