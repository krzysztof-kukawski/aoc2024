import os
import re

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day3")

with open(input_path, "r", encoding="utf8") as puzzle_file:
    puzzle_text = puzzle_file.read()

excluded = re.findall(r"(?<=don't\(\))(.*?)(?=do\(\))", puzzle_text, re.DOTALL)

for i in excluded:
    puzzle_text = puzzle_text.replace(i, "")

last_do_not = re.search(r"(don't\(\))(?!.*\1)", puzzle_text, re.DOTALL)
limit = last_do_not.span()

puzzle_text = puzzle_text[: limit[0]]

muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_text)

result = 0
for mul in muls:
    digits = re.findall(r"\((\d+,\d+)\)", mul)
    sides = digits[0].split(",")
    sides = [int(i) for i in sides]
    result += sides[0] * sides[1]

print(result)
