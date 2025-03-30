from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
# this model does not give structured output
# llm = HuggingFaceEndpoint(
#     repo_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task = 'text-generation',
#     max_new_tokens= 512,

# )

# Load environment variables from .env file
load_dotenv()

model  = ChatOpenAI(
    model=os.getenv("CHAT_GPT_MODEL")
)
template1 = PromptTemplate(
    template="""
    Write a 100 words report on {topic}""",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="""
    Write a five line summary on {text} and give them in points""",
    input_variables=["text"],
)



prompt1 = template1.invoke(input = {'topic':'blackhole'})

result = model.invoke(prompt1)

prompt2  = template2.invoke({'text' : result.content})

result2 = model.invoke(prompt2)

print(result2.content)

