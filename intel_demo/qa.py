# import re

# text = "Here is an example. Thought: This is the part I want to capture. More text follows."
# thought_match = re.search(r"Thought: (.*)", text)

# if thought_match:
#     print(thought_match.group(1))  # 输出 "This is the part I want to capture."
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))

print(a @ b.T)
