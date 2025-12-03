import math


a = 0.1 + 0.2

b = 0.3

print(a == b, math.isclose(a, b))


print(math.isnan(math.nan))


'''
备注
'''

result = 0 or [] or {} or "default"
print(result)