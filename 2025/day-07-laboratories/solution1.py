from typing import Set


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    splits = 0
    indexes = {lines[0].index("S")}

    for line in lines:
        new_indexes: Set[int] = set()

        for index in indexes:
            if line[index] == "^":
                splits += 1
                new_indexes.add(index - 1)
                new_indexes.add(index + 1)
            else:
                new_indexes.add(index)

        indexes = new_indexes

    print(splits)


solve("input-test.txt")  # 21
solve("input.txt")  # 1518
