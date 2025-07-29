from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.lazy_load()

# print(len(docs))

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)

# print(docs[0].page_content)
# print(docs[1].metadata)