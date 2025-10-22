def countdown(n):
  if n == 0:
    print('发射')
    return

  print(n)
  countdown(n - 1)

countdown(3)



def fibonacci(n):
    # 基本情况：前两个数
    if n <= 1:
        return n
    
    # 递归情况：当前数等于前两个数之和
    return fibonacci(n-1) + fibonacci(n-2)

# 测试函数
for i in range(6):
    print(f"斐波那契数列第{i}个数是：{fibonacci(i)}")


def binary_search(arr, target, left, right):
    # 基本情况：如果左边界大于右边界，说明没找到
    if left > right:
        return -1
    
    # 计算中间位置
    mid = (left + right) // 2
    
    # 如果找到目标值，返回位置
    if arr[mid] == target:
        return mid
    
    # 如果中间值大于目标值，在左半部分查找
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    
    # 如果中间值小于目标值，在右半部分查找
    return binary_search(arr, target, mid + 1, right)

# 测试函数
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(numbers, target, 0, len(numbers) - 1)
print(f"数字{target}在列表中的位置是：{result}")