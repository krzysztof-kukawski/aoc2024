import os
import re

cwd = os.path.dirname(__file__)
input_path = os.path.join(cwd, "puzzle_input_day2")

with open(input_path, "r", encoding="utf8") as puzzle_file:
    puzzle_lines = puzzle_file.readlines()

reports = []
for line in puzzle_lines:
    report = re.findall(r"\d+", line)
    report = [int(i) for i in report]
    reports.append(report)


class Report:
    def __init__(self, levels: list[int]):
        self.levels = levels
        self.increasing = None
        self.was_increasing = None
        self.decreasing = None

    def check_safe(self) -> bool:
        self.increasing = self._check_increasing()
        if not self.increasing and not self.was_increasing:
            self.decreasing = self._check_decreasing()
        if self.increasing or self.decreasing:
            return True
        return False

    def _check_increasing(self) -> bool:
        for i, level in enumerate(self.levels[1:]):
            diff = level - self.levels[i]
            if not self._check_diff(diff):
                return False
        return True

    def _check_decreasing(self) -> bool:
        for i, level in enumerate(self.levels[1:]):
            diff = self.levels[i] - level
            if not self._check_diff(diff):
                return False
        return True

    def _check_diff(self, diff: int) -> bool:
        if diff < 1 or diff > 3:
            return False
        else:
            if not self.was_increasing:
                self.was_increasing = True
        return True


safe_reports = [Report(i).check_safe() for i in reports]
print(sum(safe_reports))
