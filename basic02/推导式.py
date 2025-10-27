# 基本语法： [表达式 for 变量 in 可迭代对象 (可选的if条件)]


# 交换字典中的键和值
fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
print(fruit_colors.items())
color_fruits = {color: fruit for fruit, color in fruit_colors.items()}
print(color_fruits)  # {'red': 'apple', 'yellow': 'banana', 'purple': 'grape'}


# 列表
lst = [x + 5 for x in range(5)]
print(lst)

# 字典
dir = {a: a + 7 for a in range(5)}
print(dir)


# 生成器
gen = (x * 2 for x in range(5))
print(list(gen))
