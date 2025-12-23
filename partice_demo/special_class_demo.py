
class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # *args 可变参数 **kwargs 关键词可变参数
    def __new__(cls, *args, **kwargs):
        print(f"执行了__new__方法")
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print(f"执行了__call__方法")

    def __str__(self):
        return '哈哈哈'


foo = Foo("Foo", 19) # class在初始化时，会默认调用__new__方法
foo() # 实例对象() 会调用__call__方法
str = str(foo)
print(f"str={str}")
print(foo.__dict__) # 返回字典 {'name': 'Foo', 'age': 19}


class SqlHelper(object):
    def __init__(self, sql):
        self.sql = sql
    def __enter__(self):
        self.connection = 11
        return self.connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection = 22