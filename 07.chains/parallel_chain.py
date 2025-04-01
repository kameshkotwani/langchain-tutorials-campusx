from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
from langchain.schema.runnable import RunnableParallel
load_dotenv()

# this uses gpt 4o mini
model1 = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

# this one uses the 3.5 turbo model
model2 = ChatOpenAI()
parser = StrOutputParser()

prompt_zero = PromptTemplate(
    template="""Generate detailed report on {topic}.""",
    input_variables=["topic"],
    )


    
prompt_one =  PromptTemplate(
    template="""
    Generate short and simple notes on this following text. \n {text}.
    """,
    input_variables=["text"],

)

prompt_two =  PromptTemplate(
    template="""
    Generate a five short question answers from the following: \n {text}.
    """,
    input_variables=["text"],

)

prompt_three =  PromptTemplate(
    template="""
    Merge the provided notes and quiz into a single document: \n notes -> {notes} and quiz -> {quiz}.
    """,
    input_variables=["notes","quiz"],

)

topic_generator_chain = prompt_zero | model1 | parser

parallel_chain = RunnableParallel(
    {
        "notes": prompt_one | model1 | parser,
        'quiz': prompt_two | model2 | parser
    }
)


merge_chain = prompt_three | model1 | parser

chain  = topic_generator_chain|  parallel_chain | merge_chain

print(chain.invoke({'topic':"Python"}))

chain.get_graph().print_ascii()