from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from os import getenv
from pydantic import BaseModel, Field


load_dotenv()

class StrModel(BaseModel):
    output : str  = Field(...,description='output in the str format')

    
parser = PydanticOutputParser(pydantic_object=StrModel)

# prompt creation
prompt =PromptTemplate(
    template="""
    Write me a joke  about {topic}. {format_instructions} 
    """,
    input_variables=['topic'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
    
)

# create the model
model = ChatOpenAI(
    model=getenv('CHAT_GPT_MODEL')
)

# chain = RunnableSequence(prompt,model,parser)
chain = prompt | model | parser


result:StrModel = chain.invoke({'topic':'Python'})

print(result.output)
# print(type(result))



