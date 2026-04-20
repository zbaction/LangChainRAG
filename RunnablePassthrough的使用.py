from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的参考资料，简洁和专业的回答用户的问题。参考资料:{context}"),
        ("user", "用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

# 准备一下资料
vector_store.add_texts(["跑步对身体好","吃水果有益健康"])

input_text = "怎么减肥"

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

def print_prompt(prompt):
    print(prompt.to_string())
    print("-----------------------------")
    return prompt

def format_func(docs):
    if not docs:
        return "无参考资料"

    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
        formatted_str += "]"
    return formatted_str

chain = (
    {"input": RunnablePassthrough(),"context": retriever | format_func} | prompt | print_prompt | model | StrOutputParser()
)

res = chain.invoke(input_text)
print(res)
