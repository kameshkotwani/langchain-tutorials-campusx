from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableParallel
import os
from dotenv import load_dotenv

parser = StrOutputParser()


load_dotenv()

model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

prompt_template = PromptTemplate(
    template =  """
        Write a joke about {topic}.
    """,
    input_variables = ["topic"]
)

passthrough_chain = RunnableParallel(
    {
        'explanation': prompt_template | model | parser,
        'topic': RunnablePassthrough()
    }
)

print(passthrough_chain.invoke({'topic':'Python'}))
