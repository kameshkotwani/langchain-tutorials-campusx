from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

model  = ChatOpenAI(
    model=os.getenv("CHAT_GPT_MODEL")

)

schema = [ResponseSchema(name=f"fact_{i}",description=f"description of the fact {i}") for i in range(1,5)]


# create a parser
# disadvantage: Cannot validate data, cannot specify types
# advantage: can specify the format of the output
structured_parser:StructuredOutputParser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template="""Give me four facts about {topic}. {format_instructions}""",
    input_variables=['topic'],
    partial_variables={
        'format_instructions': structured_parser.get_format_instructions()
    }
)

chain = template | model | structured_parser

print(chain.invoke({'topic':'blackhole'}))
    

