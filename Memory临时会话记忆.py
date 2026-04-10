from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from sqlalchemy.orm.attributes import get_history

model = ChatTongyi(model="qwen3-max")

# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史：{chat_history},用户提问: {input},请回答"
# )
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史回应用户问题。"),
        MessagesPlaceholder("chat_history"),
        ("human", "请回答如下问题，{input}")
    ]
)
str_parser = StrOutputParser()



def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(), "="*20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parser

# key就是session，value就是INMemoryChatMessageHistory对象
store = {}
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

converstaion_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

if __name__ == "__main__":

    session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }
    res = converstaion_chain.invoke({"input": "小米有3只猫"}, session_config)
    print(res)

    res1 = converstaion_chain.invoke({"input": "小明有2只狗"}, session_config)
    print(res1)

    res2 = converstaion_chain.invoke({"input": "一个就几只宠物"}, session_config)
    print(res2)

