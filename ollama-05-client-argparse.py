import os
from ollama import Client
import argparse

# 使い方："python3 ファイル名.py -h" でヘルプを表示します。

# ArgumentParserオブジェクトを作成し、スクリプトの説明を追加
parser = argparse.ArgumentParser(description="指定されたオプションに従って実行するスクリプト")

# コマンドライン引数を受け取る設定。
parser.add_argument('-m', type=str, help='LLM モデル')
parser.add_argument('-s', type=open, help='システムプロンプトファイル')
parser.add_argument('-u', type=str, help='ユーザプロンプト')
parser.add_argument('-url', type=str, help='エンドポイントURL')

# 引数を解析
args = parser.parse_args()

# 変数のまとめ
# コマンドライン引数がない場合の初期値も設定
LLM_MODEL = args.m if args.m else 'gemma3:4b'
ENDPOINT_URL = args.url if args.url else 'http://localhost:11434/'
USER_PROMPT = args.u if args.u else '短い自己紹介をお願いします。'
SYSTEM_PROMPT = args.s if args.s else 'あなたは親切で賢いアシスタントです。日本語で回答してください。'


client = Client(host=ENDPOINT_URL)

print(f"ユーザプロンプト：{USER_PROMPT} \n-----")

stream = client.chat(
    model = LLM_MODEL,
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT },
        {'role': 'user', 'content': USER_PROMPT }
    ],
    stream = True
)


# ストリーミングで回答
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
