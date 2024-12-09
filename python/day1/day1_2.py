import os
import re

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day1")

with open(input_path, "r", encoding="utf8") as puzzle_file:
    puzzle_text = puzzle_file.read()

left = re.findall(r"(\d+)[ ]", puzzle_text)
right = re.findall(r"[ ](\d+)", puzzle_text)

left_distinct = set(left)


def value_counts(number: str, collection: list) -> int:
    if number in collection:
        counts = [i == number for i in collection]
        return sum(counts)
    return 0


number_counts = {
    i: (value_counts(i, right), value_counts(i, left)) for i in left_distinct
}

result = 0
for i in number_counts:
    result += int(i) * number_counts[i][0] * number_counts[i][1]

print(result)
