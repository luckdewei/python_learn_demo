from pathlib import Path

# 创建路径对象
path1 = Path('/home/user/documents')  # 绝对路径
path2 = Path('relative/path')         # 相对路径
path3 = Path.cwd()                    # 当前工作目录
path4 = Path.home()                   # 用户主目录

print(f"绝对路径: {path1}")
print(f"当前目录: {path3}")
print(f"用户主目录: {path4}")