# 字符串的创建方式
str1 = '单引号字符串'
str2 = "双引号字符串"
str3 = '''三引号可以
创建多行
字符串'''
str4 = """同样支持
多行文本"""

print(str1)
print(str2)
print(str3)
print(str4)
print(f"类型: {type(str1)}")  # <class 'str'>



text = "Hello Python Programming"

print("切片操作:")
print(f"原始字符串: '{text}'")
print(f"text[0:5]: '{text[0:5]}'")  # Hello
print(f"text[6:12]: '{text[6:12]}'")  # Python
print(f"text[:5]: '{text[:5]}'")  # Hello (从开始到索引5)
print(f"text[13:]: '{text[13:]}'")  # Programming (从索引13到结束)
print(f"text[-11:]: '{text[-11:]}'")  # Programming (从倒数第11个到结束)

# 步长切片
print(f"text[::2]: '{text[::2]}'")  # HloPto rgamn (步长为2)
print(f"text[1::2]: '{text[1::2]}'")  # el yhnPormig (从索引1开始，步长为2)
print(f"text[::-1]: '{text[::-1]}'")  # gnimmargorP nohtyP olleH (反转)

# 复杂的切片
print(f"text[0:10:2]: '{text[0:10:2]}'")  # HloPt (0到10，步长2)


s = 'ssskkk'
s[0] = 'l'