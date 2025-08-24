from ollama import Client


ENDPOINT_URL = 'http://localhost:11434'

client = Client(host=ENDPOINT_URL)

USER_PROMPT = """ あなたについて教えてください。 """

print(f"ユーザプロンプト：{USER_PROMPT} \n-----")

stream = client.chat(
    model='gemma3:4b',
    messages=[
        {
            'role': 'user',
            'content': USER_PROMPT
        }
    ],
    stream=True
)

# ストリーミングで回答
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
