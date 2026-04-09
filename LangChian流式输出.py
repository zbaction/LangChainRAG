from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# 调用invoke模型
res = model.stream(input="你会干什么")

for item in res:
    print(item,end = "",flush = True)

