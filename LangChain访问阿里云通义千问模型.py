from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# 调用invoke模型
res = model.invoke(input="请帮我写一个冒泡排序的python代码")

print(res)
