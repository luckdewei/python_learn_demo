"""
bool_	True/False 布尔值
int_ / intc / intp	平台相关的整型，intp 常用于索引
int8/16/32/64	固定字节的有符号整数
uint8/16/32/64	固定字节的无符号整数
float16/32/64 (float_)	半精度、单精度、双精度浮点数
complex64/complex128 (complex_)	由两个浮点数组成的复数
其他：timedelta64、datetime64、object_、bytes_、unicode_	处理时间、对象和文本的数据类型
"""

import numpy as np

dt = np.dtype(np.int32)

print(dt)
