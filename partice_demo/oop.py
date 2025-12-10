class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    # Used with `repr()`
    def __repr__(self):
        return f"Date({self.year},{self.month},{self.day})"


# a + b       a.__add__(b)
# a - b       a.__sub__(b)
# a * b       a.__mul__(b)
# a / b       a.__truediv__(b)
# a // b      a.__floordiv__(b)
# a % b       a.__mod__(b)
# a << b      a.__lshift__(b)
# a >> b      a.__rshift__(b)
# a & b       a.__and__(b)
# a | b       a.__or__(b)
# a ^ b       a.__xor__(b)
# a ** b      a.__pow__(b)
# -a          a.__neg__()
# ~a          a.__invert__()
# abs(a)      a.__abs__()

# len(x)      x.__len__()
# x[a]        x.__getitem__(a)
# x[a] = v    x.__setitem__(a,v)
# del x[a]    x.__delitem__(a)
