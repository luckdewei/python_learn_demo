from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        # 父类只定义接口/默认实现，一般由子类重写
        raise NotImplementedError("子类必须实现speak方法")


class Dog(Animal):
    def speak(self):
        return f"{self.name}: 汪汪！"


class Cat(Animal):
    def hello(self):
        return f"{self.name}: 喵喵！"

    # def speak(self):
    #     return f"{self.name}: 喵喵！"


dog = Dog("小黑")
cat = Cat(
    "小花"
)  # TypeError: Can't instantiate abstract class Cat without an implementation for abstract method 'speak'
print(dog.speak())  # 小黑: 汪汪！
print(isinstance(dog, Animal))  # True


# super
class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)  # 先初始化父类部分
        self.can_fly = can_fly
