# 从 langchain_text_splitters 模块导入递归字符文本分割器类
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 创建递归字符文本分割器对象，指定参数
# chunk_size 表示每块最大允许的字符数为 100
# chunk_overlap 表示块与块之间没有重叠（重叠字符数为 0）
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)

# 构造待分割的文本，包含多段各自为 99 或 100 个相同字符以及换行符
document = f"""{"1"*100}\n{"2"*99}\n\n{"3"*99}\n{"4"*99}"""

# 使用文本分割器的 split_text 方法将 document 分割为多个字符串块
texts = text_splitter.split_text(document)

# 打印一共分割出的块数
print(f"共分割为 {len(texts)} 个块：")

# 枚举输出每个块的序号及块内容（使用 repr 格式便于查看特殊字符）
for i, text in enumerate(texts, 1):
    print(i, repr(text))
