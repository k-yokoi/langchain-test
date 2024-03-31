from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

print("# 出力")
llm = OpenAI()
result = llm.invoke("自己紹介してください")
print(result)
print("\n")

print("# ストリーム出力")
for chunk in llm.stream("自己紹介してください"):
    print(chunk, end="", flush=True)

print("\n")