
class Foo(object):
    def __init__(self, name):
        self._name = name # protected 变量
        self.__age = 18 # 私有成员变量，不能直接访问
    def show_age(self): # 私有成员变量只可以间接访问
        return self.__age
    @property
    def begin(self):
        return "Begin"

    @property
    def name(self):
        return self._name


foo = Foo("Foo")
# foo.show_age()
print(f"foo._name:{foo.name}")
print(f"foo.__age:{foo.show_age()}")
print(f"foo_begin:{foo.begin}")