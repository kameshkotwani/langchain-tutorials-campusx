from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal,Optional,List
from pydantic import BaseModel,EmailStr,Field,PositiveFloat

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini-2024-07-18")

# creating a schema for how the data will be structured
# class Review(TypedDict):
#     summary: str
#     sentiment: Literal["positive", "negative", "neutral"]
#     rating: int
#     pros: list[str]
#     cons: list[str]
#     reviewer: Optional[str]
#     key_themes: Annotated[list[str],'give a list of key themes from the review']

# using Pydantic
class Review(BaseModel):
    summary:str = Field(description="A short summary of the review")
    sentiment: Literal['pos','neg','neu'] = Field(description="The sentiment of the review")
    rating: int = Field(description="The rating given by the reviewer")
    pros: Optional[List[str]] = Field(description="A list of pros mentioned in the review")
    cons: Optional[List[str]] = Field(description="A list of cons mentioned in the review")
    reviewer: Optional[str] = Field(description="The name of the reviewer")

model = model.with_structured_output(Review)

result:Optional[Review] = model.invoke("""
The hardware is great, but the software feels bloadted and slow. I would recommend it to a friend, but only if they are willing to put up with the software issues. Also the UI looks outdated and could use a refresh. Overall, I would give it a 3 out of 5 stars. by Kamesh
""")

print(result)

if result:
    with open("review_output.json", "w") as json_file:
        json_file.write(result.model_dump_json(indent=2))
