from os import path


dataPath = path.join('./basic03/data.txt')


with open(dataPath, 'r', encoding='utf-8') as file:
  print(file.read())



# 覆盖写入模式
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# 追加写入模式
with open('output.txt', 'a', encoding='utf-8') as file:
    file.write("This line is appended.\n")