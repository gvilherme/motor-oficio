SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "Você é um assistente útil e tem a função de interpretar ofícios. "
        "Sua entrada será um texto puro contendo o ofício na íntegra. "
        "Você deve interpretar o texto e gerar uma saída estruturada no formato JSON."
    ),
}
RESPONSE_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "interpretacao_oficio",
        "schema": {
            "type": "object",
            "properties": {
                "oficio_valido": {"type": "boolean"},
                "interpretacoes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "acao": {"type": "string"},
                            "necessidades_da_acao": {
                                "type": "array",
                                "items": {"type": "object"},
                            },
                        },
                        "additionalProperties": False,
                        "required": ["acao"],
                    },
                },
            },
            "required": ["interpretacoes", "oficio_valido"],
            "additionalProperties": False,
        },
        "strict": False,
    },
}

from src.services.llm.openai_integration import consultar_openai


class EntradaAgent:
    def __init__(self):
        self.messages = [SYSTEM_MESSAGE]

    def interpretar(self, entrada):
        self.messages.append({"role": "user", "content": entrada})

        response = consultar_openai(self.messages, response_format=RESPONSE_FORMAT)
        self.messages.append({"role": "assistant", "content": response})

        return response
