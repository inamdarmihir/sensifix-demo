from langchain import PromptTemplate

from prompt_templates import (
  validation_template,
  category_l1_template,
  category_l2_template,
  ticket_template,
  response_template,
  spanish_response_template,
  korean_response_template
)

validation_prompt = PromptTemplate(
  input_variables = ["examples", "user_input"],
  template = validation_template
)


category_l1_prompt = PromptTemplate(
    template = category_l1_template,
    input_variables = ["examples", "user_input"]
)

category_l2_prompt = PromptTemplate(
    template = category_l2_template,
    input_variables = ["categories", "examples", "user_input"]
)

ticket_prompt = PromptTemplate(
  input_variables = ["examples", "user_input"],
  template = ticket_template
)


response_prompt = PromptTemplate(
  input_variables=["examples", "user_input"],
  template=response_template
)


response_prompt_spanish = PromptTemplate(
  input_variables=["examples", "user_input"],
  template=spanish_response_template  
)


response_prompt_korean = PromptTemplate(
  input_variables=["examples", "user_input"],
  template=korean_response_template  
)
