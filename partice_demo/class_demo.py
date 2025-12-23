

class Base(object):
    def __init__(self):
        pass
    def fn1(self):
        print("Base fn1")
    def fn2(self):
        print("Base fn2")
        self.fn1()
    def fn3(self):
        print("Base fn3")
        self.fn1()


class Foo(Base):
    def fn1(self):
        print(f"Foo fn1")
    def fn2(self):
        print(f"Foo fn2")

class Bar(Foo, Base):
    def fn1(self):
        print(f"Bar fn1")



bar = Bar()
bar.fn2()
bar.fn3()
