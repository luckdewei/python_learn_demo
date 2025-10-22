# 位置参数

def calculate_area(length, width):
  return length * width

# 调用函数
print(calculate_area(5, 3))  # 输出：15

# 默认参数
def print_student_info(name, grade="一年级", school="阳光小学"):
  print(f"姓名：{name}")
  print(f"年级：{grade}")
  print(f"学校：{school}")

# 只传入必填参数
print_student_info("小明")  # 使用默认的年级和学校


# 可变位置参数： 处理不确定数量的参数

"""
可变参数是指在函数定义时使用*args形式, 允许函数接收任意数量的位置参数,
这些参数会被打包成一个元组传入函数内部。
"""
def calculate_total_score(*scores):

    print(type(scores))
    total = 0  # 初始化总分
    for score in scores:  # 遍历所有分数
        total += score  # 累加分数
    return total  # 返回总分

# 测试不同数量的参数
print(calculate_total_score(85, 90, 95))  # 输出：270
print(calculate_total_score(100, 100))    # 输出：200
print(calculate_total_score(80))          # 输出：80


# 命名关键字参数

"""
命名关键字参数是指在函数定义时使用*和参数名来限制参数名称，
这样在调用函数时必须使用参数名传入参数。
创建一个更严格的学生信息记录函数：
"""

def register_student(name, age, *, address, phone):
    # 星号（*）在这里的作用是分隔位置参数和命名关键字参数
    # 星号前面的name和age是位置参数，可以按位置传递
    # 星号后面的address和phone是命名关键字参数，调用时必须使用参数名
    # 这样设计可以强制调用者明确指定address和phone的参数名，避免参数顺序混淆导致的错误
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"住址：{address}")
    print(f"电话：{phone}")

# 正确的调用方式
register_student("小明", 10, address="北京市", phone="12345678")

# 接收任意数量的关键字参数


def create_student_profile(
        name, age=10, #必填参数
        *scores, #可接收任意数量的可变位置参数
        address, #命名关键字参数
        **other_info #可接收任意数量的可变关键字参数
        ):
    """
    创建学生档案
    name: 姓名（必填）
    age: 年龄（默认10岁）
    *scores: 各科成绩（可变参数）
    address: 家庭住址（命名关键字参数）
    **other_info: 其他信息（可变命名关键字参数）
    """
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print("成绩：")
    for i, score in enumerate(scores, 1):
        print(f"科目{i}：{score}")
    print(f"住址：{address}")
    print("其他信息：")
    for key, value in other_info.items():
        print(f"- {key}: {value}")

# 调用函数
create_student_profile(
    "小明",                    # 必填参数
    11,                       # 修改默认年龄
    85, 90, 95,              # 三个成绩
    address="北京市",         # 命名关键字参数
    hobby="足球",             # 关键字参数
    talent="钢琴"             # 关键字参数
)