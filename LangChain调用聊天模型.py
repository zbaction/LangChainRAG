from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatTongyi(model="qwen3-max")

# 准备消息列表
messages = [
    SystemMessage(content="你是一个浪漫主义诗人"),
    HumanMessage(content="写一首诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="按照这个格式，再写一首诗"),
]

# 调用stream流式输出
res = model.stream(input=messages)

# 打印内容
for chunk in res:
    print(chunk.content,end = "",flush = True)


