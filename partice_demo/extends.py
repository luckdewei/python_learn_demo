


class C(object):
    pass

class B(object):
    pass
class A(B, C):
    pass

# 展示类的继承链
print(A.__mro__) # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(A.mro()) # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

