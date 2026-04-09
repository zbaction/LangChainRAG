from langchain_community.embeddings import DashScopeEmbeddings

embeddings = DashScopeEmbeddings()

print(embeddings.embed_query("你好"))
print(len(embeddings.embed_query("你好")))
print(embeddings.embed_documents(["你好", "世界"]))


