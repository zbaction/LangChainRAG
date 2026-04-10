from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser


first_prompt = PromptTemplate.from_template(
    "我姓{lastname},我的{gender}出身了,请起一个名字,并封装为json的格式输出，key是name，value是你起名字的内容。请严格按照格式输出"

)

second_prompt = PromptTemplate.from_template(
    "我的女生名字是{name},请帮我解析一下它的含义。"
)

json_parser = JsonOutputParser()
str_parser = StrOutputParser()

model = ChatTongyi(model="qwen3-max")

chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# res = chain.invoke({"lastname": "张", "gender": "女"})
# print(res)
# print(type(res))

# 流式输出
for chunk in chain.stream({"lastname": "张", "gender": "女"}):
    print(chunk, end="", flush=True)