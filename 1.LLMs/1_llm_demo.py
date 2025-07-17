from langchain import OpenAI
from dotenv import load_dotenv 

load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo", temperature=0)
output = llm.invoke("What is the capital of India")

print(output)