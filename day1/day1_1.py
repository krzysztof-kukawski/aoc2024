import os
import re

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day1")

with open(input_path, 'r', encoding="utf8") as puzzle_file:
    puzzle_text = puzzle_file.read()

left = re.findall(r"(\d+)[ ]", puzzle_text)
right = re.findall(r"[ ](\d+)", puzzle_text)

left = [int(i) for i in left]
right = [int(i) for i in right]

left = sorted(left)
right = sorted(right)

result = 0
for i, j in enumerate(left):
    result += abs(j - right[i])

print(result)
