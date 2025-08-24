import os
from ollama import Client
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 変数のまとめ
LLM_MODEL = os.getenv('LLM_MODEL')
ENDPOINT_URL = os.getenv('ENDPOINT_URL')
USER_PROMPT = os.getenv('USER_PROMPT')
SYSTEM_PROMPT = os.getenv('SYSTEM_PROMPT')

client = Client(host=ENDPOINT_URL)

print(f"ユーザプロンプト：{USER_PROMPT} \n-----")

stream = client.chat(
    model=LLM_MODEL,
    messages=[
        {'role': 'system', 'content': SYSTEM_PROMPT },
        {'role': 'user', 'content': USER_PROMPT }
        ],
    stream=True
)

# ストリーミングで回答
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
