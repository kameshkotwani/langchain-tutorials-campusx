from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableLambda
import os
from dotenv import load_dotenv



def total_words(text):
    return len(text.split())

load_dotenv()

model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

prompt = PromptTemplate(
    template="""
    Write a joke about {topic}.
    """,
    input_variables=["topic"]
)

parallel_chain = RunnableParallel(
    {
        'joke': prompt | model | StrOutputParser(),
        'total_words': prompt | model | StrOutputParser() | RunnableLambda(total_words)
    }
)
result = parallel_chain.invoke({'topic':'Python'})

print(result)