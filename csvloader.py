from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(file_path="data/books.csv")
docs=loader.load()
print(docs)