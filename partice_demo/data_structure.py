# 空类型
email_adress = None

# 元组 -- 一旦定义无法改变
s = ("GOOD", 100, 490.1)
# 特殊情况
t = ()  # An empty tuple
w = ("GOOG",)  # A 1-item tuple 要加逗号
# 元组获取数据
name = s[0]  # 'GOOG'
shares = s[1]  # 100
price = s[2]  # 490.1
# 元组拆包
name, shares, price = s
print("Cost", shares * price)


# 列表和元组的区别
record = ("GOOG", 100, 490.1)  # A tuple representing a record in a portfolio
symbols = ["GOOG", "AAPL", "IBM"]  # A List representing three stock symbols

# 字典

d = {"name": "GOOG", "shares": 100, "price": 490.1}
print(d["name"], d["shares"])
# 修改添加
d["shares"] = 75
d["date"] = "6/6/2007"
# 删除
del d["date"]

print(f"dict:{d}")
print(f"{d.keys()}")
print(f"{d.items()}")
# 字典的键必须是不可变类型
holidays = {
    (1, 1): "New Years",
    (3, 14): "Pi day",
    (9, 13): "Programmer's day",
}
print(f"holidays:{holidays}")


# 列表: 当数据顺序很重要时，请使用列表。记住，列表可以存储任何类型的对象。例如，包含元组的列表：
portfolio = [("GOOG", 100, 490.1), ("IBM", 50, 91.3), ("CAT", 150, 83.44)]
# 列表构建
records = []
records.append(("GOOG", 100, 490.10))
records.append(("IBM", 50, 91.3))
print(f"records:{records}")

# 集合 Set--集合是互异且无序的数据
tech_stocks = {"IBM", "AAPL", "MSFT"}
# Alternative syntax
tech_stocks = set(["IBM", "AAPL", "MSFT"])

names = ["IBM", "AAPL", "GOOG", "IBM", "GOOG", "YHOO"]
unique = set(names)
unique.add("CAT")  # Add an item
unique.remove("YHOO")  # Remove an item

# enumerate() 函数
# enumerate 函数为迭代添加一个额外的计数值
names = ["Elwood", "Jake", "Curtis"]
for i, name in enumerate(names, 1):
    print(f"i:{i} name:{name}")

# zip 函数
columns = ["name", "shares", "price"]
values = ["GOOG", 100, 490.1]
pairs = zip(columns, values)  # ('name','GOOG'), ('shares',100), ('price',490.1)
print(f"pairs:{list(pairs)}")
print(f"pairs:{dict(zip(columns, values))}")

# 列表方法
a = [1, 2, 3, 4, 5]
b = [2 * x for x in a]
print(b)
# 过滤
a1 = [1, -5, 4, 2, -2, 10]
c = [2 * x for x in a1 if x > 0]
print(f"c:{c}")
