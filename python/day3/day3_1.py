import os
import re

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day3")

with open(input_path, "r", encoding="utf8") as puzzle_file:
    puzzle_text = puzzle_file.read()

muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_text)

result = 0
for mul in muls:
    digits = re.findall(r"\((\d+,\d+)\)", mul)
    sides = digits[0].split(",")
    sides = [int(i) for i in sides]
    result += sides[0] * sides[1]

print(result)
