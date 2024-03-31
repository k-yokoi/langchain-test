import pprint
from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import OpenAI

load_dotenv()


model = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.0)


class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the dish")
    steps: list[str] = Field(description="steps to make the dish")

parser = PydanticOutputParser(pydantic_object=Recipe)

prompt = PromptTemplate(
    template="料理のレシピを考えてください。\n{format_instructions}\n料理名： {dish}\n",
    input_variables=["dish"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

prompt_and_model = prompt | model
output = prompt_and_model.invoke({"dish": "カレーライス"})
recipe = parser.invoke(output)
print(output)
pprint.pprint(recipe)