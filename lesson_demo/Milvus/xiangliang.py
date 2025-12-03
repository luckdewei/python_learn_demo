# 导入数学库用于数学运算
import math

# 导入类型注解 Tuple
from typing import Tuple


# 定义函数，计算二维向量 (x, y) 的长度
def vector_length(x: float, y: float) -> float:
    # 调用 math.hypot 计算两数的欧几里得长度
    return math.hypot(x, y)


# 定义函数，计算二维向量 (x, y) 与 x 轴的夹角（以角度为单位）
def vector_direction(x: float, y: float) -> float:
    # 使用 atan2 计算夹角，再用 degrees 转换为角度
    return math.degrees(math.atan2(y, x))


# 定义函数，计算从点 a 到点 b 的向量
def vector_from_points(
    a: Tuple[float, float], b: Tuple[float, float]
) -> Tuple[float, float]:
    # 返回 b 点减去 a 点得到的向量 (x2-x1, y2-y1)
    return b[0] - a[0], b[1] - a[1]
