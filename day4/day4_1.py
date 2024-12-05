import os


class Xmas:
    def __init__(self):
        cwd = os.path.dirname(__file__)
        input_path = os.path.join(cwd, "puzzle_input_day4")

        with open(input_path, "r", encoding="utf8") as puzzle_file:
            puzzle_text = puzzle_file.readlines()

        self.puzzle_text = [line.replace("\n", "") for line in puzzle_text]

    def search(self) -> int:
        locs = self.get_locations_of_xs(self.puzzle_text)
        letters = ["M", "A", "S"]

        checks = {}
        for i, letter in enumerate(letters):
            checks[letter] = self.check_direction(i + 1)

        puzzle_result = 0
        for loc in locs:
            loc_result = self.check_set_of_letters(loc, checks)
            transposed = self.transpose_results(loc_result)

            for i in transposed:
                if all(i):
                    puzzle_result += 1
        return puzzle_result

    @staticmethod
    def transpose_results(results: list[list[bool]]) -> list[list[bool]]:
        transposed = []
        for i in range(8):
            partial = []
            for result in results:
                partial.append(result[i])
            transposed.append(partial)
        return transposed

    @staticmethod
    def get_locations_of_xs(words: list[str]) -> list[tuple[int, int]]:
        locations = []
        for i, line in enumerate(words):
            for j, letter in enumerate(line):
                if letter == "X":
                    locations.append((j, i))
        return locations

    @staticmethod
    def check_direction(number: int) -> list[tuple[int, int]]:
        res = []
        for i in (-number, 0, number):
            for j in (-number, 0, number):
                if j != 0 or i != 0:
                    res.append((i, j))
        return res

    def check_set_of_letters(
        self, start: tuple, set_of_letters: dict[str, list]
    ) -> list[list[bool]]:
        results = []
        for i in set_of_letters:
            directions = set_of_letters[i]
            results.append(self.check_set_of_directions(start, directions, i))
        return results

    def check_set_of_directions(
        self, start: tuple, directions: list[tuple], letter: str
    ) -> list[bool]:
        results = []
        for i in directions:
            results.append(self.check_single_spot(start, i, letter))
        return results

    def check_single_spot(self, start: tuple, directions: tuple, letter: str) -> bool:
        try:
            x = start[0] + directions[0]
            y = start[1] + directions[1]
            if x < 0 or y < 0:
                return False
            return self.puzzle_text[y][x] == letter

        except IndexError:
            return False


print(Xmas().search())
