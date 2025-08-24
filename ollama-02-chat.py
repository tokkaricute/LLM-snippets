from ollama import chat

USER_PROMPT = """ あなたについて教えてください。 """

print(f"ユーザプロンプト：{USER_PROMPT} \n-----")

stream = chat(
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
