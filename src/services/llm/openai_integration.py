from openai import OpenAI

client = OpenAI()

# Função para enviar prompt ao modelo da OpenAI
def consultar_openai(messages, model="gpt-4o-mini", response_format=None):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=200,
        response_format=response_format
    )
    return response.choices[0].message.content