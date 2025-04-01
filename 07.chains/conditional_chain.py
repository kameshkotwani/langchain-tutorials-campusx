from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
import os
from pydantic import BaseModel,Field
load_dotenv()

class Sentiment(BaseModel):
    sentiment: str = Field(...,description="The sentiment of the message either positive or negative")

    @property
    def sentiment_(self):
        return self.sentiment

# this uses gpt 4o mini
model1 = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

pydantic_parser = PydanticOutputParser(pydantic_object=Sentiment)
# this one uses the 3.5 turbo model
parser = StrOutputParser()

prompt = PromptTemplate(
    template="""Classify the sentiment of the following feedback text into positive or negative: {feedback}.\n {format_instructions}""",
    input_variables=["feedback"],
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}

)

classifier_chain = prompt | model1 | pydantic_parser

prompt2 = PromptTemplate(
    template= """ write an appropriate response to this feedback text: {feedback}""",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment_ == 'positive',prompt2 | model1 | parser),
    (lambda x: x.sentiment_ == 'negative',prompt2 | model1 | parser),
    RunnableLambda( lambda x : "could not find sentiment")
)

chain  = classifier_chain | branch_chain

print(chain.invoke({
    'feedback':"This is a neutral statement"
}))
chain.get_graph().print_ascii()
