from ollama import chat

USER_PROMPT = """ あなたについて教えてください。 """

print(f"ユーザプロンプト：{USER_PROMPT} \n-----")

response = chat(
    model='gemma3:4b',
    messages=[
        {
            'role': 'user',
            'content': USER_PROMPT
        }
    ]
)

print(response['message']['content'])
