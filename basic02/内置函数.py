'''
# 数学类
# abs() - 返回绝对值
print(abs(-5))      # 5
print(abs(3.14))    # 3.14

# round() - 四舍五入
print(round(3.14159, 2))  # 3.14
print(round(3.5))         # 4

# pow() - 幂运算
print(pow(2, 3))     # 8
print(pow(2, 3, 5))  # 3 (2^3 % 5)

# divmod() - 返回商和余数
quotient, remainder = divmod(10, 3)
print(quotient, remainder)  # 3 1


# 枚举和打包
# enumerate() - 枚举索引和元素
foods = ["apple", "banana", "pear"]
for idx, food in enumerate(foods):
    print(idx, food)        # 0 apple, 1 banana, 2 pear

# zip() - 并行打包多个序列
names = ['Tom', 'Jerry']
ages = [8, 9]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# range()  range(start, stop, step)
# 基本用法
for i in range(5):
    print(i, end=" ")  # 输出: 0 1 2 3 4

for i in range(3, 8):
    print(i, end=" ")  # 输出: 3 4 5 6 7

for i in range(0, 10, 2):
    print(i, end=" ")  # 输出: 0 2 4 6 8

for i in range(5, 0, -2):
    print(i, end=" ")  # 输出: 5 3 1


# enumerate(iterable, start=0) 返回枚举对象，包含索引和值

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 输出:
# 0 apple
# 1 banana
# 2 cherry

# 自定义起始索引
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
# 输出:
# 1 apple
# 2 banana
# 3 cherry


# zip(*iterables) 并行遍历多个可迭代对象，将相同位置的元素打包成元组

names = ['Tom', 'Jerry', 'Spike']
scores = [95, 98, 88]
for name, score in zip(names, scores):
    print(name, score)
# 输出:
# Tom 95
# Jerry 98
# Spike 88

# 序列解包
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)  # ('a', 'b', 'c')
print(numbers)  # (1, 2, 3)

# 注意事项
# 如果传入的可迭代对象长度不同，则以最短的为准
# 多余的元素被忽略

from functools import reduce
# reduce(func, iterable[, initial]) 对可迭代对象执行累积计算，需要从 functools 导入。


# 带初始值
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)  # 20 (10 + 1 + 2 + 3 + 4)

'''
# 自定义排序

# 使用key参数进行复杂排序
words = ['apple', 'banana', 'cherry', 'date']
# 按字符串长度排序
print(sorted(words, key=len))  # ['date', 'apple', 'banana', 'cherry']

# 按字符串长度降序排序
print(sorted(words, key=len, reverse=True))  # ['banana', 'cherry', 'apple', 'date']
print(words)