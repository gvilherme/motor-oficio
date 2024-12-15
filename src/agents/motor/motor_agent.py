SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "Você é um assistente útil e tem acesso à algumas funções externas, como bloqueio e desbloqueio, "
        "mas o conjunto exato de funções disponíveis pode variar, e será fornecido de forma estruturada para você "
        "via mensagens."
        "Sua entrada será um texto estruturado no formato json, você deve interpretar o json, e verificar se as ações "
        "solicitadas são possíveis dado as funções externas habilitadas, e então gerar uma saída também estruturada "
        "de forma que o payload contenha dados para a execução das ações possíveis."
    ),
}
RESPONSE_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "acoes_motor",
        "schema": {
            "type": "object",
            "properties": {
                "existem_acoes_possiveis": {"type": "boolean"},
                "acoes_possiveis": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nome_acao": {"type": "string"},
                            "payload": {"type": "object", "additionalProperties": True},
                        },
                        "required": ["nome_acao", "payload"],
                        "additionalProperties": False,
                    },
                },
                "existem_acoes_impossiveis": {"type": "boolean"},
                "acoes_impossiveis": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nome_acao": {"type": "string"},
                            "observacao": {"type": "string"},
                        },
                        "required": ["nome_acao", "observacao"],
                        "additionalProperties": False,
                    },
                },
                "observacao": {"type": "string"},
            },
            "required": ["existem_acoes_possiveis", "acoes_possiveis"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}

from src.services.llm.openai_integration import consultar_openai

class MotorAgent:
    def __init__(self):
        self.messages = [SYSTEM_MESSAGE]

    def interpretar(self, entrada):
        self.messages.append(entrada)
        response = consultar_openai(self.messages, response_format=RESPONSE_FORMAT)
        self.messages.append(response)
        return response