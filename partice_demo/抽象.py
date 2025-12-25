from abc import ABC, abstractmethod


# py 需要借助 abc 来实现抽象接口
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        pass
