# CSV（逗号分隔值）文件是常见的表格数据格式，适合数据交换和存储。
import csv

# 写入 CSV 文件
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["姓名", "年龄", "城市"])  # 写入表头
    writer.writerow(["张三", "25", "北京"])  # 写入数据
    writer.writerow(["李四", "30", "上海"])

# 读取 CSV 文件
with open("data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
