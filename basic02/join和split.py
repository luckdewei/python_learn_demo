# join() and split()


s = "hello world"
print(s.split())

# 使用 maxsplit 参数
record = "id,name,age,gender"
print(record.split(",", maxsplit=2))  # ['id', 'name', 'age,gender']


fruits = ["apple", "banana", "orange", "grape"]
print("字符串列表:", fruits)

strs = ",".join(fruits)
print("使用逗号连接:", strs)


tuple1 = ("apple", "banana", "orange", "grape")

str2 = "-".join(tuple1)

print("使用 - 连接:", str2)
