import os
from ollama import Client
from dotenv import load_dotenv
import argparse

# 使い方："python3 ファイル名.py -h" でヘルプを表示します。

# .envファイルを読み込む
load_dotenv()

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
# 優先度：コマンドライン引数 > dotenvファイル
LLM_MODEL = args.m if args.m else os.getenv('LLM_MODEL')
ENDPOINT_URL = args.url if args.url else os.getenv('ENDPOINT_URL')
USER_PROMPT = args.u if args.u else os.getenv('USER_PROMPT')
SYSTEM_PROMPT = args.s if args.s else os.getenv('SYSTEM_PROMPT')


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
