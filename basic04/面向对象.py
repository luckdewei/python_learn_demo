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
