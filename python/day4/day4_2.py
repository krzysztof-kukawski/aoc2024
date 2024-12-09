import os

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day4")

with open(input_path, "r", encoding="utf8") as puzzle_file:
    puzzle_text = puzzle_file.readlines()

puzzle_text = [line.replace("\n", "") for line in puzzle_text]


def get_locations_of_as(words: list[str]) -> list[tuple[int, int]]:
    locations = []
    for i, line in enumerate(words):
        for j, letter in enumerate(line):
            if letter == "A":
                locations.append((j, i))
    return locations


def check_direction():
    res = []
    for i in ((-1, -1), (1, 1), (1, -1), (-1, 1)):
        res.append(i)
    return res


def check_single_spot(start: tuple, directions: tuple) -> str | None:
    try:
        x = start[0] + directions[0]
        y = start[1] + directions[1]
        if x < 0 or y < 0:
            return None
        if puzzle_text[y][x] in ("X", "A"):
            return None
        return puzzle_text[y][x]

    except IndexError:
        return None


def check_set_of_directions(start: tuple, directions: list[tuple]):
    results = []
    for i in directions:
        results.append(check_single_spot(start, i))
    return results


locs = get_locations_of_as(puzzle_text)
checks = check_direction()

result = 0
for loc in locs:
    cross = check_set_of_directions(loc, checks)

    if cross[0] != cross[1] and cross[2] != cross[3]:
        if all(cross):
            result += 1
print(result)
