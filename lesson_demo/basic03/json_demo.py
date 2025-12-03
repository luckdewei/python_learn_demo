import json

# 准备数据
data = {"name": "张三", "age": 25, "cities": ["北京", "上海", "广州"]}

# 写入 JSON 文件
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 读取 JSON 文件
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(loaded_data)
