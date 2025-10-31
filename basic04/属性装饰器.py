"""
在 Python 中，可以通过 @property 装饰器，将实例方法变成属性访问的方式，
从而优雅地控制获取和设置过程。这种写法既保留了属性式的易用，
又提供了逻辑控制点和数据验证，非常适合对类中的私有（或受保护）属性做封装。

为什么用属性装饰器？
- 安全性提升：避免直接暴露内部数据，防止属性被非法赋值
- 易于维护：随时可以在 getter/setter 内添加校验、自动处理等逻辑
- 统一接口：外部代码和普通属性一样调用，无需显式函数调用
"""


class Demo:
    def __init__(self, value):
        self._value = value  # 习惯上受保护（单下划线）

    # 定义 value 属性的 getter 方法
    @property
    def value(self):
        return self._value

    # 定义 value 属性的 setter 方法
    @value.setter
    def value(self, new_value):
        # 检查 new_value 是否为 int 类型且值为非负
        if isinstance(new_value, int) and new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("value 必须为非负整数")


# 创建实例
d = Demo(5)
print(d.value)  # 相当于 d.value()，自动调用@property修饰的方法，输出 5
d.value = 10  # 相当于 d.value(10)，自动调用 setter
# d.value = -3    # 会抛出 ValueError


# 只写 @property，不写 setter，则属性为只读：
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius**2


c = Circle(2)
print(c.area)  # 12.56
# c.area = 10   # 报错：只读属性
