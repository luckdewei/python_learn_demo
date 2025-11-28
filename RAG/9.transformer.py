# -*- coding: utf-8 -*-
# 说明：验证 Sentence Transformers 是否安装成功

# 说明：导入 SentenceTransformer 类
from sentence_transformers import SentenceTransformer
import os

os.environ["HUGGINGFACE_HUB_CACHE"] = "./my_models"
os.environ["HF-ENDPOINT"] = "https://hf-mirror.com"
# 说明：尝试加载一个轻量级模型进行测试
# "all-MiniLM-L6-v2" 是一个小型的通用模型，适合快速测试
# 首次运行时会自动下载模型（可能需要一些时间）
print("正在加载模型进行测试...")
model = SentenceTransformer("all-MiniLM-L6-v2")
# C:\Users\rensh\.cache\huggingface\hub\models--sentence-transformers--all-MiniLM-L6-v2
# 说明：对一个简单的句子进行编码测试
sentence = "这是一个测试句子"
embedding = model.encode(sentence)

# 说明：检查嵌入向量的形状
print(f"安装成功！嵌入向量维度：{embedding.shape}")
print(f"前 9 个维度值：{embedding[:9]}")

# 说明：如果没有报错并输出了维度信息，说明安装成功
