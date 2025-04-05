from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class SummaryParser(BaseModel):
    summary: str = Field(...,description='summary of the text')

parser = PydanticOutputParser(pydantic_object=SummaryParser)

model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

summary_prompt = PromptTemplate(
    template = """ Generate a 100 words summary on why learning {topic} is important. {format_instructions}""",
    input_variables = ['topic'],
    partial_variables = {
        'format_instructions': parser.get_format_instructions()
    }
)
joke_prompt = PromptTemplate(
    template = """ write a joke on why learning {topic} is important. {format_instructions}""",
    input_variables = ['topic'],
    partial_variables = {
        'format_instructions': parser.get_format_instructions()
    }
)
motivational_prompt = PromptTemplate(
    template = """ write a motivational quote on why learning {topic} is important. {format_instructions}""",
    input_variables = ['topic'],
    partial_variables = {
        'format_instructions': parser.get_format_instructions()
    }
)

summary_chain = summary_prompt | model | parser
joke_chain = joke_prompt | model | parser
motivational_chain = motivational_prompt | model | parser

parallel_chain = RunnableParallel(
    {
        'summary': summary_chain,
        'joke': joke_chain,
        'motivational': motivational_chain
    }
)

result = parallel_chain.invoke({'topic':'Math'})
print(result.get('summary'))
print(result.get('joke'))
print(result.get('motivational'))