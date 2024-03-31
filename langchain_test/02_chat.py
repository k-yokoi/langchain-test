from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="こんにちは！私はジョンです。"),
    AIMessage(content="はじめまして！ジョンさん。どのようにお手伝いしましょうか？"),
    HumanMessage(content="私の名前がわかりますか？"),
]

print("# 出力")
result = chat.invoke(messages)
print(result.content)
print("\n")

print("# ストリーム出力")
for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)

print("\n")