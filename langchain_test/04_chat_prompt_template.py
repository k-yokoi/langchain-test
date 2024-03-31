from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは{country}料理のプロフェッショナルです。"),
        ("human", "以下の料理のレシピを考えてください。\n\n料理名: {dish}"),
    ]
)

messages = chat_template.format_messages(country="イギリス", dish="肉じゃが")

print(messages)