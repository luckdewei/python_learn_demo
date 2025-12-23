from collections.abc import Iterable, Iterator

# 迭代器对象
class IT(object):
    def __init__(self):
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.counter += 1
        if self.counter >= 10:
            raise StopIteration
        return self.counter

obj = IT()

# v1 = obj.__next__()
# v2 = obj.__next__()
# v3 = obj.__next__()
v1 = next(obj)
v2 = next(obj)
v3 = next(obj)
print(v1)
print(v2)
print(v3)

for x in obj:
    print(f"x:{x}")

print(isinstance(obj, Iterable))