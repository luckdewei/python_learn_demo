add = lambda x, y: x + y

print(add(3, 5))


# 用lambda表达式将列表中的每个数都翻倍
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # 对每个元素都乘以2
print(doubled)  # 输出: [2, 4, 6, 8]