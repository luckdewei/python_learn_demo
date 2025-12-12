class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        """计算股票总价值"""
        return self.shares * self.price

    def sell(self, nshares):
        """卖出股票"""
        if nshares > self.shares:
            raise ValueError("卖出份额不能超过持有份额")
        self.shares -= nshares

    # 特殊方法开始
    def __repr__(self):
        """用于开发者查看的字符串表示"""
        return f"Stock({self.name!r}, {self.shares}, {self.price})"

    def __str__(self):
        """用于用户查看的字符串表示"""
        return f"{self.name}: {self.shares}股 @ ￥{self.price:.2f}"

    def __add__(self, other):
        """实现股票合并的加法操作"""
        if self.name != other.name:
            raise ValueError("只能合并同名股票")
        return Stock(
            self.name, self.shares + other.shares, (self.price + other.price) / 2
        )

    def __len__(self):
        """返回持有股票数量"""
        return self.shares

    def __getitem__(self, key):
        """通过属性名访问"""
        if key == "name":
            return self.name
        elif key == "shares":
            return self.shares
        elif key == "price":
            return self.price
        else:
            raise KeyError(f"未知属性: {key}")


# 演示代码
if __name__ == "__main__":
    print("=== 创建股票实例 ===")
    s1 = Stock("GOOG", 100, 490.10)
    s2 = Stock("GOOG", 50, 485.30)

    # 演示 __repr__ 和 __str__
    print("\n=== 字符串表示演示 ===")
    print("repr输出:", repr(s1))
    print("str输出:", str(s1))
    print("直接打印:", s1)  # 默认调用 __str__

    # 演示 __add__
    print("\n=== 股票合并演示 ===")
    combined = s1 + s2
    print("合并后:", combined)

    # 演示 __len__
    print("\n=== 持有量演示 ===")
    print(f"持有 {len(s1)} 股 {s1.name}")

    # 演示 __getitem__
    print("\n=== 属性访问演示 ===")
    print("股票名称:", s1["name"])
    print("股票价格:", s1["price"])

    # 演示绑定方法
    print("\n=== 绑定方法演示 ===")
    cost_method = s1.cost  # 获取绑定方法
    print("绑定方法:", cost_method)
    print("调用绑定方法:", cost_method())

    # 演示属性访问函数
    print("\n=== 属性访问函数演示 ===")
    print("使用getattr获取名称:", getattr(s1, "name"))
    print("检查属性是否存在:", hasattr(s1, "price"))
    print("检查不存在的属性:", hasattr(s1, "dividend"))
