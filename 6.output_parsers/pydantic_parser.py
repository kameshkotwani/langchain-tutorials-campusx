from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv


class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person",gt=18,lt=100)
    city: Optional[str] = Field(default=None, description="City of the person")
    net_worth: Optional[float] = Field(default=None, description="Net worth of the person")
    source: Optional[str] = Field(default=None, description="Source of the response")

parser = PydanticOutputParser(pydantic_object=Person)

# Load environment variables from .env file
load_dotenv()

model  = ChatOpenAI(
    model=os.getenv("CHAT_GPT_MODEL")

)

template = PromptTemplate(
    template="""Give me a name, age, city and net_worth in billions of richest person in {country}. {format_instructions}""",
    input_variables=['country'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

user_input = input("Enter the country: ")
print(template.invoke({'country':user_input}))
chain = template | model | parser
result =chain.invoke({'country':user_input})
print(result)
print(type(result))