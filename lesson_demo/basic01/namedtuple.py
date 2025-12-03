from collections import namedtuple

# namedtuple 具名元组 的使用
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
x = p._replace(x=3)
y = p._replace(y=4)
print(p)
print(p.x)
print(p.y)
print(p[0])
print(p[1])
print(p._fields)
print(x)
print(y)
