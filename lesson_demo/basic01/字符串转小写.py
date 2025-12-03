# casefold()与lower()方法的区别
print("=== casefold()与lower()方法的区别 ===")

# 测试字符串
test_strings = ["straße", "Grüße", "Café", "İstanbul", "ΣΟΦΙΑ", "Hello World"]

print("字符串\t\tlower()\t\tcasefold()")
print("-" * 50)

for string in test_strings:
    lower_result = string.lower()
    casefold_result = string.casefold()
    print(f"'{string}'\t\t'{lower_result}'\t\t'{casefold_result}'")

# 国际化字符串比较
print("\n=== 国际化字符串比较 ===")


def case_insensitive_compare_lower(str1, str2):
    """使用lower()进行不区分大小写的比较"""
    return str1.lower() == str2.lower()


def case_insensitive_compare_casefold(str1, str2):
    """使用casefold()进行不区分大小写的比较"""
    return str1.casefold() == str2.casefold()


# 测试比较
test_pairs = [
    ("straße", "STRASSE"),
    ("Grüße", "GRÜSSE"),
    ("Café", "CAFÉ"),
    ("İstanbul", "ISTANBUL"),
]

for str1, str2 in test_pairs:
    lower_result = case_insensitive_compare_lower(str1, str2)
    casefold_result = case_insensitive_compare_casefold(str1, str2)
    print(f"'{str1}' == '{str2}':")
    print(f"  lower()比较: {lower_result}")
    print(f"  casefold()比较: {casefold_result}")
    print()
