# 定义基础的股票类
class Stock:
    # 初始化方法，创建股票实例时需要提供名称、份额和价格
    def __init__(self, name, shares, price):
        self.name = name  # 股票名称
        self.shares = shares  # 持有份额
        self.price = price  # 股票价格

    # 计算股票总价值的方法
    def cost(self):
        return self.shares * self.price

    # 卖出股票的方法
    def sell(self, nshares):
        if nshares > self.shares:
            raise ValueError("卖出份额不能超过持有份额")
        self.shares -= nshares  # 减少持有份额


# 定义继承自Stock的子类
class MyStock(Stock):
    # 恐慌性抛售方法，会卖出所有股票
    def panic(self):
        self.sell(self.shares)  # 调用父类的sell方法卖出全部股票

    # 重写父类的cost方法，增加1.25倍系数
    def cost(self):
        # 使用super()调用父类的cost方法，然后乘以1.25
        return 1.25 * super().cost()


# ===== 演示基础Stock类的使用 =====
print("=== 基础Stock类演示 ===")
# 创建Stock实例：谷歌股票，100股，每股490.10元
goog_stock = Stock("GOOG", 100, 490.10)
print(f"初始状态: {goog_stock.name}, {goog_stock.shares}股 @ ￥{goog_stock.price:.2f}")
print(f"股票总价值: ￥{goog_stock.cost():.2f}")

# 卖出25股
goog_stock.sell(25)
print(f"卖出25股后剩余: {goog_stock.shares}股")

# ===== 演示MyStock类的使用 =====
print("\n=== MyStock子类演示 ===")
# 创建MyStock实例：苹果股票，50股，每股145.30元
apple_stock = MyStock("AAPL", 50, 145.30)
print(
    f"初始状态: {apple_stock.name}, {apple_stock.shares}股 @ ￥{apple_stock.price:.2f}"
)
print(f"基础计算价值: ￥{apple_stock.shares * apple_stock.price:.2f}")
print(f"MyStock计算价值(含1.25倍系数): ￥{apple_stock.cost():.2f}")

# 演示panic方法
print(f"\n恐慌抛售前: {apple_stock.shares}股")
apple_stock.panic()
print(f"恐慌抛售后: {apple_stock.shares}股")

# ===== 错误处理演示 =====
print("\n=== 错误处理演示 ===")
try:
    # 尝试卖出超过持有量的股票(当前持有75股，尝试卖出100股)
    goog_stock.sell(100)
except ValueError as e:
    print(f"错误发生: {e}")
