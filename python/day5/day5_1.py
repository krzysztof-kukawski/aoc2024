import os
import re

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day5")

with open(input_path, "r", encoding="utf8") as puzzle_file:
    puzzle_text = puzzle_file.readlines()

rules = []
for i in puzzle_text:
    rule = re.findall(r"(\d+)\|(\d+)", i)
    if rule:
        rules.append(rule[0])

updates = []
for i in puzzle_text:
    update = i if "," in i else None
    if update:
        update = update.replace("\n", "")
        update = update.split(",")
        updates.append(update)


def check_rules(single_update: list[str], ruleset: list[tuple[str, str]]) -> bool:
    for single_rule in ruleset:
        if single_rule[0] in single_update and single_rule[1] in single_update:
            if single_update.index(single_rule[0]) > single_update.index(
                single_rule[1]
            ):
                return False
    return True


def get_middle_part(single_update: list[str]) -> int:
    idx = len(single_update) // 2
    return int(single_update[idx])


result = 0
for update in updates:
    is_correct = check_rules(update, rules)
    if is_correct:
        middle = get_middle_part(update)
        result += middle

print(result)
