from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./data/python基础语法.txt",encoding="utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, # 分段的最大字符数
    chunk_overlap=50, # 分段之间的重叠字符数
    separators=["\n\n","\n"],
    length_function=len  # 统计字符的依据函数

)

split_docs = splitter.split_documents(docs)
print(len(split_docs))