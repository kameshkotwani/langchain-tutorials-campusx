from langchain_core.prompts import PromptTemplate

template_=  """
Write a {type} of the paper {research_paper} in {length_of_reply} length.

"""
template = PromptTemplate(
     template= template_,
     input_variables=[
            'research_paper',
            'type',
            'length_of_reply',
     ],
     validate_template=True
)

template.save('template.json')