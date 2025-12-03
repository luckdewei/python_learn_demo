# 可变参数（位置参数）
def show_args(*args):
  print(f"参数类型：{type(args)}")
  print(f"参数内容：{args}")

show_args(1, 2, 3)

show_args('a', 'b', 'c')

# 可变参数（关键词参数）
def show_kwargs(**kwargs):
    print(f"参数类型: {type(kwargs)}")
    print(f"参数内容: {kwargs}")

show_kwargs(a=1, b=2, c=3)