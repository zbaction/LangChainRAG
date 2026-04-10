from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate

template = PromptTemplate.from_template("他的名字是{name},爱好是{habby}")

res = template.format(name="小明",habby="打篮球")
print(res,type(res))

res1 = template.invoke(input={"name": "小明", "habby": "打篮球"})
print(res1,type(res1))