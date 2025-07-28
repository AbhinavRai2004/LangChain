from langchain_community.document_loaders import TextLoader

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(f"Loaded {len(docs)} documents.")
print(docs[0].page_content)  # Display the content of the first document
print(docs[0].metadata)  # Display the metadata of the first document if available
