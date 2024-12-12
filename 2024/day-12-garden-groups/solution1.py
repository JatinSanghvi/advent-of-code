from collections import deque
from typing import Set, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Surround the garden to simplify checks.
    size = len(lines)
    garden = [] + ["." + line + "." for line in (["." * size] + lines + ["." * size])]

    # Enlist all fences.
    fences: Set[Tuple[float, float]] = set()
    for row in range(size + 1):
        for col in range(size + 1):
            if garden[row][col] != garden[row + 1][col]:
                fences.add((row + 0.5, col))
            if garden[row][col] != garden[row][col + 1]:
                fences.add((row, col + 0.5))

    price = 0
    reached: Set[Tuple[int, int]] = set()

    # Perform breadth first search to discover regions.
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if (row, col) not in reached:
                area = 0
                perimeter = 0

                reached.add((row, col))
                queue = deque([(row, col)])

                while queue:
                    row1, col1 = queue.popleft()
                    area += 1

                    for row2, col2 in [(row1 - 1, col1), (row1, col1 - 1), (row1, col1 + 1), (row1 + 1, col1)]:
                        if ((row1 + row2) / 2, (col1 + col2) / 2) in fences:
                            perimeter += 1
                        elif (row2, col2) not in reached:
                            reached.add((row2, col2))
                            queue.append((row2, col2))

                price += area * perimeter

    print(price)


solve("input-test-1.txt")  # 140
solve("input-test-2.txt")  # 772
solve("input-test-3.txt")  # 1930
solve("input.txt")  # 1461752
