import os
from datetime import datetime

# 获取文件详细信息
info = os.stat("output.txt")

print(info)
