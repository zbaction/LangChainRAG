from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

prompt = PromptTemplate.from_template(
    "我的同学是:{name},喜欢{habby}"
)

model = ChatTongyi(model="qwen3-max")
parser = StrOutputParser()

chain = prompt | model | parser | model | parser

res:str = chain.invoke({"name": "小明", "habby": "打篮球"})
print(type(res))