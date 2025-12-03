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

# 嵌套循环
# 二维列表展开
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, [10, 11, 12]]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 等价于：
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)


# 生成器表达式的优势

# 内存效率对比
import sys

n = 100000
# 列表推导式 - 立即创建所有元素
list_comp = [x**2 for x in range(n)]
# 生成器表达式 - 惰性计算
gen_expr = (x**2 for x in range(n))

print(f"列表推导式内存: {sys.getsizeof(list_comp)} 字节")  # 800984 字节
print(f"生成器表达式内存: {sys.getsizeof(gen_expr)} 字节")  # 200 字节
