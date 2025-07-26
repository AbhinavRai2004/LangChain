from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import re

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)

# Prompt template
prompt = PromptTemplate(
    template="Give 5 most interesting points about: {topic}",
    input_variables=["topic"]
)

# Model
model = ChatHuggingFace(llm=llm)

# Output parser
parser = StrOutputParser()

# Chain
chain = prompt | model | parser

# Invoke
output = chain.invoke({"topic": "LangChain"})


cleaned_output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL)
print(cleaned_output.strip())