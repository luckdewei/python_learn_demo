"""
鸭子类型（Duck Typing）是一种动态类型检查的方法，广泛应用于Python等动态编程语言中。
它的核心理念源于一句谚语："如果它走起来像鸭子，叫起来也像鸭子，那它就是一只鸭子。"

从编程角度来看，鸭子类型关注的是对象的行为（即它有哪些方法和属性），而不是它实际的类型（即它继承自哪个类）。
这意味着，只要一个对象提供了某个方法或属性，我们就可以像对待拥有该方法或属性的任何其他对象一样使用它，而无需
关心它的具体类或接口。这种机制使得编写的代码更加灵活和简洁。
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def eat(self):
        pass


dog = Dog("Dog")
dog.eat()
