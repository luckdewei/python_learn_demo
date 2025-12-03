# 定义一个简单的装饰器，在函数执行前打印日志
def log(func):
    def wrapper(*args, **kw):
        print('开始执行函数:', func.__name__)  # 打印函数名
        result = func(*args, **kw)  # 调用原函数，* 和 ** 在这里起到解包作用
        print('函数执行完毕')  # 打印结束信息
        return result  # 返回原函数的结果
    return wrapper  # 返回包装后的函数

# 使用装饰器
@log# 定义一个简单的装饰器，在函数执行前打印日志
def log(func):
    def wrapper(*args, **kw):
        print('开始执行函数:', func.__name__)  # 打印函数名
        result = func(*args, **kw)  # 调用原函数，* 和 ** 在这里起到解包作用
        print('函数执行完毕')  # 打印结束信息
        return result  # 返回原函数的结果
    return wrapper  # 返回包装后的函数

# 使用装饰器
@log
def hello(name, age,**kw):
    print(name, age, kw)

hello('张三', 20,city='上海', job='工程师')  
#开始执行函数: hello
#张三 20 {'city': '上海', 'job': '工程师'}
#函数执行完毕
def hello(name, age,**kw):
    print(name, age, kw)

hello('张三', 20,city='上海', job='工程师')  
#开始执行函数: hello
#张三 20 {'city': '上海', 'job': '工程师'}
#函数执行完毕