from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    # file_path="./data/stu.json",
    # jq_schema=".hobby.[0,1]",
    # text_content=False

    # file_path="./data/stus.json",
    # jq_schema=".[].name"

    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,
    json_lines=True
)

documents = loader.load()
print(documents)
