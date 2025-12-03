from os import path


dataPath = path.join("./basic03/data.txt")


with open(dataPath, "r", encoding="utf-8") as file:
    print(file.read())


# 覆盖写入模式
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# 追加写入模式
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("This line is appended.\n")


# 分块读取大文件
with open("large_file.txt", "r", encoding="utf-8") as file:
    while True:
        chunk = file.read(1000)  # 每次读取1000个字符
        if not chunk:  # 读取结束
            break
        print(chunk)


# 读取二进制文件
with open("image.jpg", "rb") as file:
    chunk = file.read(1024)  # 读取1024字节
    print(chunk)


# 批量写入字符串

# 准备要写入的字符串列表
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

# 使用 writelines() 批量写入
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

# 或者使用循环写入
with open("output.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line)
