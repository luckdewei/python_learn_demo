# 演示Python类和封装
class Stock:
    # 使用__slots__限制可添加的属性
    __slots__ = ("_name", "_shares", "_price")

    def __init__(self, name, shares, price):
        # 使用下划线前缀表示私有属性
        self._name = name
        self.shares = shares  # 通过property设置
        self._price = price

    @property
    def name(self):
        """name属性的getter，只读属性"""
        return self._name

    @property
    def shares(self):
        """shares属性的getter"""
        return self._shares

    @shares.setter
    def shares(self, value):
        """shares属性的setter，带有类型检查"""
        if not isinstance(value, int):
            raise TypeError("Expected an integer for shares")
        if value < 0:
            raise ValueError("Shares cannot be negative")
        self._shares = value

    @property
    def price(self):
        """price属性的getter"""
        return self._price

    @price.setter
    def price(self, value):
        """price属性的setter，带有值检查"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def cost(self):
        """计算属性，计算股票总价值"""
        return self.shares * self.price

    def sell(self, amount):
        """卖出股票的方法"""
        if amount > self.shares:
            raise ValueError("Not enough shares to sell")
        self.shares -= amount


# 使用示例
print("创建股票实例:")
s = Stock("AAPL", 50, 145.0)
print(f"初始状态: {s.name}, {s.shares}股, 单价${s.price:.2f}, 总价值${s.cost:.2f}")

print("\n尝试修改shares:")
try:
    s.shares = 75  # 合法修改
    print(f"修改后shares: {s.shares}")

    s.shares = "一百"  # 非法修改，会抛出TypeError
except TypeError as e:
    print(f"错误: {e}")

print("\n尝试卖出股票:")
s.sell(25)
print(f"卖出25股后: {s.shares}股剩余")

print("\n尝试添加非法属性:")
try:
    s.prices = 150.0  # 由于__slots__限制，会抛出AttributeError
except AttributeError as e:
    print(f"错误: {e}")

print("\n尝试修改只读属性:")
try:
    s.name = "Microsoft"  # name是只读属性
except AttributeError as e:
    print(f"错误: {e}")

print("\n最终状态:")
print(f"{s.name}, {s.shares}股, 单价${s.price:.2f}, 总价值${s.cost:.2f}")
