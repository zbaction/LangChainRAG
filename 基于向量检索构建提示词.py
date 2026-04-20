from langchain_community.chat_models import ChatTongyi
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

result = vector_store.similarity_search(input_text,2)

reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

def print_prompt(prompt):
    print(prompt.to_string())
    print("-----------------------------")
    return prompt

chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({"input":input_text,"context":reference_text})

print(res)