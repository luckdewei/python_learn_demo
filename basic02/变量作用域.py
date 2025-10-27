'''
作用域类型	描述	示例
局部作用域	变量在函数内部定义，只能在该函数内部使用	函数内的局部变量
全局作用域	变量在所有函数体外部定义，可以在整个模块里访问	模块级别的变量
嵌套作用域	内部函数可以访问外部函数中的变量	闭包中的外部变量
内置作用域	Python预先定义的内置标识符	len, range, print等
'''

# python 采用LEGB原则查找变量：
# L: Local（本地作用域）
# E: Enclosing（嵌套函数的外部函数作用域）
# G: Global（全局作用域）
# B: Built-in（内置作用域）
'''
name = "全局变量"

def outer():
    name = "外部函数变量"
    def inner():
        name = "内部函数变量"
        print(name)  # 输出"内部函数变量"
    inner()
    print(name)      # 输出"外部函数变量"

outer()
print(name)          # 输出"全局变量"



# global 关键字允许我们在函数内部声明某个变量为全局变量，从而可以在函数内部修改它
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2


# nonlocal关键字用于在嵌套函数中声明变量来自最近的一层非全局作用域（外层函数）
def outer():
    x = "local"
    
    def inner():
        nonlocal x  # 声明 x 来自外层作用域
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
# inner: nonlocal
# outer: nonlocal
'''