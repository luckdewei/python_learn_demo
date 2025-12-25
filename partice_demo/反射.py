# 反射 提供一种更加灵活的方式让你实现去对象中操作成员（以字符串的形式去对象中进行成员操作）
"""
函数	描述	返回值
hasattr(obj, name)	检查对象是否有指定属性	布尔值
getattr(obj, name[, default])	获取对象属性值	属性值或默认值
setattr(obj, name, value)	设置对象属性值	None
delattr(obj, name)	删除对象属性	None
dir(obj)	获取对象所有属性和方法	列表
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("老cc", 19)

print(hasattr(p1, "name"))
print(getattr(p1, "age"))
