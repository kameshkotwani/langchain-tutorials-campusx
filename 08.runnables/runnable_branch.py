from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableBranch
import os
from dotenv import load_dotenv

def word_count(text):
    return len(text.split())

load_dotenv()
parser = StrOutputParser()
model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

prompt1 = PromptTemplate(
    template =""" Write a detailed report on the {topic}""",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template =""" Summarise the following {topic} in fifty words""",
    input_variables=["topic"]
)

report_generation_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 200, prompt2 | model | parser ),
    (RunnablePassthrough())
)
final_chain =  report_generation_chain | branch_chain

print(final_chain.invoke({'topic':'Russia v Ukraine'}))
