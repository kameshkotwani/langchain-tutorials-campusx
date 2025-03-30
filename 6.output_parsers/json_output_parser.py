from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# create a parser
json_parser = JsonOutputParser()
# Load environment variables from .env file
load_dotenv()

model  = ChatOpenAI(
    model=os.getenv("CHAT_GPT_MODEL")
)

template1 = PromptTemplate(
    template="""
    Give me a name, age, and city of a fictional character. {format_instructions}
""",
    input_variables=[],
    partial_variables={
        'format_instructions': json_parser.get_format_instructions()
    }
)
template2 = PromptTemplate(
    template="""
    Give me a 50 words report on {topic}. {format_instructions}
""",
    input_variables=['topic'],
    partial_variables={
        'format_instructions': json_parser.get_format_instructions()
    }
)



prompt = template2.invoke({'topic':'blackhole'})
print(prompt)

# result = model.invoke(prompt)
# print(json_parser.parse(result.content))

# using chains

chain = template2 | model | json_parser

print(chain.invoke({'topic':'blackhole'}))
