class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# class Portfolio:
#     def __init__(self):
#         self.holdings = []  # 持有股票的列表

#     def add_stock(self, stock):
#         self.holdings.append(stock)

#     def __iter__(self):
#         return iter(self.holdings)  # 返回列表的迭代器


class Portfolio:
    def __init__(self, holdings=[]):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    def add_stock(self, stock):
        self._holdings.append(stock)

    @property
    def total_cost(self):
        return sum([s.shares * s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares


# 创建投资组合
portfolio = Portfolio()
portfolio.add_stock(Stock("IBM", 100, 120.5))
portfolio.add_stock(Stock("MSFT", 50, 210.7))
portfolio.add_stock(Stock("AAPL", 30, 145.2))

# 使用for循环迭代投资组合中的股票
for stock in portfolio:
    print(f"股票: {stock.name}, 数量: {stock.shares}, 价格: {stock.price}")
