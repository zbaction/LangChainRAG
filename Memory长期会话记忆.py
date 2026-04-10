import os,json

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from typing import Sequence


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path,self.session_id)
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    from typing import Sequence

    def add_message(self, message: BaseMessage) -> None:
        all_messages = list(self.messages)
        all_messages.append(message)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([message_to_dict(m) for m in all_messages], f, ensure_ascii=False, indent=4)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([message_to_dict(m) for m in all_messages], f, ensure_ascii=False, indent=4)

    @property
    def messages(self)-> list[BaseMessage]:
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                messages = json.load(f)
                return messages_from_dict(messages)
        except FileNotFoundError:
            return []

    def clear(self)-> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)

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
    return FileChatMessageHistory(session_id,"./chat_history")

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
    # res = converstaion_chain.invoke({"input": "小米有3只猫"}, session_config)
    # print(res)
    #
    # res1 = converstaion_chain.invoke({"input": "小明有2只狗"}, session_config)
    # print(res1)

    res2 = converstaion_chain.invoke({"input": "一个就几只宠物"}, session_config)
    print(res2)

