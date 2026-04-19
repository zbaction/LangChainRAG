from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path= "./data/a202cd30-6f61-4b89-985f-ea7fb87dfc57.pdf",
    mode="page" # 默认是page
)

i = 0
for doc in loader.lazy_load():
    print(doc)
    i += 1
    print("------------------",i)