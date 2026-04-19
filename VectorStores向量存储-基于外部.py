from langchain_core import documents
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8"

)

documents = loader.load()

# 向量存储的新增
vector_store.add_documents(
    documents = documents,
    ids = ["id" + str(i) for i in range(1,len(documents)+1)],
    vector_store = vector_store
)

# 删除
vector_store.delete(["id1"])

# 检索
result = vector_store.similarity_search(
    "我爱python",
    3
)

print(result)
