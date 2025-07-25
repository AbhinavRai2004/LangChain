from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re

from dotenv import load_dotenv

load_dotenv()

# Model
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Prompt template
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

# Chain
chain = prompt1 | model | parser | prompt2 | model | parser

# Invoke
output = chain.invoke({'topic': 'Unemployment in India'})

print(output)

chain.get_graph().print_ascii()