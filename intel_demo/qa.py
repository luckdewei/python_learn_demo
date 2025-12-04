import re

text = "Here is an example. Thought: This is the part I want to capture. More text follows."
thought_match = re.search(r"Thought: (.*)", text)

if thought_match:
    print(thought_match.group(1))  # 输出 "This is the part I want to capture."
