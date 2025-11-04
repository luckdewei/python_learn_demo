str = "Hello World"

# 使用切片操作
reversed_str1 = str[::-1]
print(reversed_str1)

# 使用join+reversed
reversed_str2 = "".join(reversed(str))
print(reversed_str2)

# 使用for循环
reversed_str3 = ""
for char in str:
    reversed_str3 = char + reversed_str3
print(reversed_str3)


# 使用递归
def reverse_str4(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str4(s[1:]) + s[0]


reversed_str4 = reverse_str4(str)
print(reversed_str4)
