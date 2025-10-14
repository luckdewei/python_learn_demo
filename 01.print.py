import time

# 语法：
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数说明：
# *objects	-	可接受多个参数，自动用空格分隔	print("A", "B", "C") → A B C
# sep	' '	多个对象之间的分隔符	print("A", "B", sep="-") → A-B
# end	'\n'	输出结束时添加的字符	print("Hi", end="!") → Hi!
# file	sys.stdout	输出目标（文件对象或流）	print("text", file=open("log.txt", "w"))
# flush	False	是否立即刷新输出缓冲区

# 1. 基础打印

print("---基础打印---\n")
print("你好🤣")

# 2. 多值打印
name = "张三"
age = 18

print("---多值打印---\n")
print("姓名:", name, "年龄:", age)

# 3. 参数


# 3.1 分隔符
print("---分隔符---\n")
print("A", "B", "C", sep=",")
print("年", "月", "日", sep="-")

# 3.2 结束符
print("---结束符---\n")
print("hello everyone", end="!\n")

# 3.3 输出到文件
print("---输出到文件---\n")

with open("log.txt", "w", encoding="utf-8") as f:
    print("xxxx", file=f)

# 3.3 flush
# print("---是否立即刷新输出缓冲区---\n")
# print("开始", end="")
# time.sleep(2)
# print("结束")

# print("开始", end="", flush=True)
# time.sleep(2)
# print("结束", flush=True)

# print("下载中", end="", flush=True)
# for i in range(5):
#     time.sleep(0.5)
#     print(".", end="", flush=True)
# print(" 完成！")


# 4. 格式化输出

# 4.1 f-string(推荐) Python 3.6+ 推荐的字符串格式化方式，
# 语法简洁、可读性强。在字符串前加上 f，并用花括号 {} 包含变量或表达式。

print("---f-string---\n")
name = "Bob"
age = 30
score = 96.145
print(f"姓名:{name}, 年龄:{age}")
# 分数格式化
print(f"分数:{score:.1f}")
print(f"分数:{score:.2f}")
# 对齐和填充
print(f"{name:>10}")  # 右对齐，宽度10:        Bob
print(f"{name:<10}")  # 左对齐，宽度10: Bob
print(f"{name:^10}")  # 居中对齐: Bob
# 进制转换
num = 255
print(f"十进制: {num}, 十六进制: {num:x}, 二进制: {num:b}")
