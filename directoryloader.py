from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
loader=DirectoryLoader(path="pdfs",glob="*.pdf",loader_cls=PyPDFLoader)
docs=loader.load()
print(len(docs))