# try:
#     x = int(input("请输入一个整数: "))
#     y = 10 / x
#     print("结果:", y)
# except ValueError:
#     print("输入的不是有效整数！")
# except ZeroDivisionError:
#     print("不能除以零！")
# except:
#     print("其他异常！")
# finally:
#     print("程序结束！")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为零！")
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError as e:
    print("发生异常：", e)


try:
    result = "3" + 4
    print("结果是:", result)
except TypeError as e:
    print("发生异常：", e)
