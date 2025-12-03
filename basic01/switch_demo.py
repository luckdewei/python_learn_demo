# python 没有原生的 switcth

# if-elif-else结构：最直接的方法，适合简单的条件判断
# 字典映射：推荐的方法，利用字典的键值对映射实现高效的条件分支
# 函数字典：在字典中存储函数对象，实现复杂的逻辑处理
# Python 3.10+ match语句：现代Python提供的模式匹配语法


def switch_if_elif(case):
    # 根据不同的 case 值返回相应的结果
    if case == "A":
        return "Case A"
    elif case == "B":
        return "Case B"
    elif case == "C":
        return "Case C"
    else:
        return "Default case"


# 测试 if-elif-else 方法
result = switch_if_elif("A")
print(f"if-elif-else 结果: {result}")
# 输出: Case A

result = switch_if_elif("D")
print(f"if-elif-else 结果: {result}")

# 字典映射 推荐


def switch_dict(case):
    # 定义映射字典
    switcher = {"A": "Case A", "B": "Case B", "C": "Case C"}
    # 使用 get 方法获取值，如果不存在则返回默认值
    return switcher.get(case, "Default case")


# 测试字典映射方法
result = switch_dict("B")
print(f"字典映射结果: {result}")
# 输出: Case B

result = switch_dict("X")
print(f"字典映射结果: {result}")
# 输出: Default case


#  使用函数字典（复杂逻辑处理)
def case_a():
    """
    处理 case A 的函数
    """
    return "Action for case A"


def case_b():
    """
    处理 case B 的函数
    """
    return "Action for case B"


def case_default():
    """
    处理默认情况的函数
    """
    return "Default action"


def switch_function_dict(case):
    """
    使用函数字典实现 switch 功能
    适合需要执行复杂逻辑的场景
    """
    # 定义函数映射字典
    switcher = {"A": case_a, "B": case_b}
    # 获取对应的函数，如果不存在则使用默认函数
    func = switcher.get(case, case_default)
    # 调用函数并返回结果
    return func()


# 测试函数字典方法
result = switch_function_dict("A")
print(f"函数字典结果: {result}")
# 输出: Action for case A

result = switch_function_dict("Z")
print(f"函数字典结果: {result}")
# 输出: Default action


# match 语句 python 3.10+


def switch_match(case):
    """
    使用 Python 3.10+ 的 match 语句实现 switch 功能
    这是最现代和强大的方法
    """
    # 使用 match 语句进行模式匹配
    match case:
        case "A":
            return "Case A"
        case "B":
            return "Case B"
        case "C":
            return "Case C"
        case _:  # 默认情况
            return "Default case"


# 测试 match 语句方法
result = switch_match("C")
print(f"match 语句结果: {result}")
# 输出: Case C

result = switch_match("Unknown")
print(f"match 语句结果: {result}")
# 输出: Default case
