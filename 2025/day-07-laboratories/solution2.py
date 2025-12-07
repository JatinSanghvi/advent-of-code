from collections import defaultdict
from typing import DefaultDict


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    indexes: DefaultDict[int, int] = defaultdict(int)
    indexes[lines[0].index("S")] = 1

    for line in lines:
        new_indexes: DefaultDict[int, int] = defaultdict(int)

        for index, count in indexes.items():
            if line[index] == "^":
                new_indexes[index - 1] += count
                new_indexes[index + 1] += count
            else:
                new_indexes[index] += count

        indexes = new_indexes

    timelines = sum(indexes.values())
    print(timelines)


solve("input-test.txt")  # 40
solve("input.txt")  # 25489586715621
