from langchain_classic.smith.evaluation.name_generation import adjectives
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

from LangChainRAG.LangChain访问阿里云通义千问模型 import model

prompt_template = PromptTemplate.from_template(
    "我的邻居是一个{adjectives}的人，他总是{behavior}。我觉得他很{feeling}。"
)

# 调用.format方法注入信息
prompt_text = prompt_template.format(adjectives="友好", behavior="帮助别人", feeling="开心")

model = Tongyi(model="qwen-max")
res = model.invoke(input=prompt_text)
print(res)

# chain = prompt_template | model
#
# res = chain.invoke(input={"adjectives": "友好", "behavior": "帮助别人", "feeling": "开心"})
# print(res)