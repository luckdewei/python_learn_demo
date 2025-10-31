"""
class 类名:
    def __init__(self, 属性1, 属性2):
        self.属性1 = 属性1
        self.属性2 = 属性2

    def 方法名(self):
        # 方法体
        pass

# 创建对象（实例化）
对象名 = 类名(参数1, 参数2)
"""


class Student:
    def __init__(self, name, age, score):
        self.name = name  # 实例属性
        self.age = age
        self.score = score

    def introduce(self):
        print(f"我是{self.name}，今年{self.age}岁，分数{self.score}")

    def is_pass(self):
        return self.score >= 60


# 创建一个学生对象
stu1 = Student("Alice", 20, 85)
stu1.introduce()  # 输出：我是Alice，今年20岁，分数85
print(stu1.is_pass())  # True


class Student:
    def __init__(self, name):
        self.name = name  # 公开属性 public
        self._nickname = name  # 受保护属性 protected
        self.__realname = name  # 私有属性 private


# 创建实例
stu = Student("小明")

# 公开属性，直接访问
print(stu.name)  # 小明
stu.name = "小红"
print(stu.name)  # 小红

# 受保护属性（实际能访问，但约定不要在类外直接访问）
print(stu._nickname)  # 小明
stu._nickname = "小亮"
print(stu._nickname)  # 小亮

# 私有属性，不能直接访问
# print(stu.__realname)  # AttributeError，不能直接访问

# 可以通过特殊方式访问私有属性（不推荐）
print(stu._Student__realname)  # 小明
