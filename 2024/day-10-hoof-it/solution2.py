from collections import defaultdict
from typing import Dict, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Counts of all 9-positions reachable from current position.
    reachables: Dict[Tuple[int, int], int] = {}

    # Intialize the counts for the trivial case of 9 as current positions.
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "9":
                reachables[(row, col)] = 1

    # Keep updating the counts until we reach 0 as current position.
    for this_char in "876543210":
        new_reachables: Dict[Tuple[int, int], int] = defaultdict(int)
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == this_char:
                    for next_row, next_col in [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]:
                        if (next_row, next_col) in reachables:
                            new_reachables[(row, col)] += reachables[(next_row, next_col)]

        reachables = new_reachables

    # Sum of counts of 9-positions reachable for each 0 as current position.
    print(sum(reachable for reachable in reachables.values()))


solve("input-test.txt")  # 81
solve("input.txt")  # 1694
