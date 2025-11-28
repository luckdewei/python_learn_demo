# -*- coding: utf-8 -*-
# 说明：快速体验 Sentence Transformers 的基本用法

# 说明：导入 SentenceTransformer 类
"""
from sentence_transformers import SentenceTransformer

# 说明：加载一个预训练的模型
# "all-MiniLM-L6-v2" 是一个轻量级的通用模型，具有以下特点：
# - 向量维度：384
# - 速度快，适合学习和测试
# - 支持多种语言（包括中文）
# 首次加载时会自动下载模型（可能需要几分钟）
print("正在加载模型 'all-MiniLM-L6-v2'...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("模型加载完成！")

# 说明：准备一个示例句子
# 这可以是任何文本，比如一句话、一段话等
sentence = "自然语言处理可以帮助我们理解文本含义"

# 说明：对句子进行编码，将文本转换为向量
# encode() 方法接受字符串或字符串列表
# 返回的是 numpy 数组（numpy.ndarray）
embedding = model.encode(sentence)

# 说明：查看嵌入向量的信息
# shape 属性显示向量的维度（这里应该是 (384,) 表示 384 维向量）
print(f"\n嵌入向量维度：{embedding.shape}")

# 说明：打印向量的前 5 个数值
# 向量中的每个数值都是浮点数，通常在 -1 到 1 之间
print(f"前 5 个维度值：{embedding[:5]}")

# 说明：打印向量的类型
print(f"向量类型：{type(embedding)}")

# 说明：查看向量中数值的范围
import numpy as np

print(f"向量数值范围：[{np.min(embedding):.4f}, {np.max(embedding):.4f}]")

"""

# -*- coding: utf-8 -*-
# 说明：演示如何批量编码多个句子

# 说明：导入 SentenceTransformer 类
from sentence_transformers import SentenceTransformer

# 说明：加载模型
# 可以重用同一个模型对象，不需要重复加载
model = SentenceTransformer("all-MiniLM-L6-v2")

# 说明：准备多条句子
# 这是一个字符串列表，每个元素是一个句子
# 在实际场景中，这些句子可能来自文件、数据库或用户输入
sentences = [
    "深度学习是人工智能的重要分支",
    "我喜欢在周末读技术博客",
    "今天的天气非常适合散步",
    "Python 是数据科学常用语言",
]

# 说明：批量编码所有句子
# encode() 方法可以接受字符串列表
# 返回的是一个二维 numpy 数组：
# - 行数 = 句子数量（这里是 4）
# - 列数 = 向量维度（这里是 384）
embeddings = model.encode(sentences)

# 说明：查看嵌入矩阵的形状
# shape 返回 (行数, 列数)，即 (句子数, 向量维度)
print(f"嵌入矩阵形状：{embeddings.shape}")
print(f"句子数量：{embeddings.shape[0]}")
print(f"向量维度：{embeddings.shape[1]}")

# 说明：访问第一条句子的向量
print(f"\n第一条句子的向量（前 5 维）：{embeddings[0][:5]}")

# 说明：遍历所有句子的向量
print("\n所有句子的向量：")
for i, sentence in enumerate(sentences):
    print(f"{i+1}. '{sentence}' -> 向量维度：{embeddings[i].shape}")
