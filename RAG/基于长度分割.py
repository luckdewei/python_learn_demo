from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")

document = f"""{"1"*50}{"2"*50}{"3"*50}"""

texts = text_splitter.split_text(document)

print(f"原文长度", len(document))
print(f"分割为", len(texts))

for i, text in enumerate(texts, 1):
    print(f"{i}:{text}")
