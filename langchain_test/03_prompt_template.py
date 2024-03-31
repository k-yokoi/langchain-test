from langchain.prompts import PromptTemplate

template = """
以下の料理のレシピを考えてください。

料理名: {dish}
"""

prompt_template = PromptTemplate.from_template(template)
result = prompt_template.format(dish="カレーライス")

print(result)