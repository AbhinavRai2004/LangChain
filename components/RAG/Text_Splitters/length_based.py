from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
    separator=''
)


res = splitter.split_documents(docs)

print(res[1].page_content)