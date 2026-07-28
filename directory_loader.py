from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = list(loader.lazy_load())

print(type(docs))
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)

print(docs[1].page_content)
print(docs[1].metadata)

print(docs[677].page_content)
print(docs[677].metadata)