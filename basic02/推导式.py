# 交换字典中的键和值
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
print(fruit_colors.items())
color_fruits = {color: fruit for fruit, color in fruit_colors.items()}
print(color_fruits)  # {'red': 'apple', 'yellow': 'banana', 'purple': 'grape'}

