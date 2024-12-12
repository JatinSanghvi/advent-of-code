from collections import deque
from typing import Set, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Surround the garden to simplify checks.
    size = len(lines)
    garden = [] + ["." + line + "." for line in (["." * size] + lines + ["." * size])]

    price = 0
    reached: Set[Tuple[int, int]] = set()

    # Perform breadth first search to discover and  each region.
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if (row, col) not in reached:
                plant = garden[row][col]
                area = 0
                corners = 0

                queue = deque([(row, col)])
                reached.add((row, col))

                while queue:
                    row1, col1 = queue.popleft()
                    area += 1

                    # Inward corners.
                    corners += (
                        (garden[row1 - 1][col1] != plant and garden[row1][col1 - 1] != plant)
                        + (garden[row1 - 1][col1] != plant and garden[row1][col1 + 1] != plant)
                        + (garden[row1 + 1][col1] != plant and garden[row1][col1 - 1] != plant)
                        + (garden[row1 + 1][col1] != plant and garden[row1][col1 + 1] != plant)
                    )

                    # Outward corners.
                    corners += (
                        (garden[row1 - 1][col1] == plant and garden[row1][col1 - 1] == plant and garden[row1 - 1][col1 - 1] != plant)
                        + (garden[row1 - 1][col1] == plant and garden[row1][col1 + 1] == plant and garden[row1 - 1][col1 + 1] != plant)
                        + (garden[row1 + 1][col1] == plant and garden[row1][col1 - 1] == plant and garden[row1 + 1][col1 - 1] != plant)
                        + (garden[row1 + 1][col1] == plant and garden[row1][col1 + 1] == plant and garden[row1 + 1][col1 + 1] != plant)
                    )

                    for row2, col2 in [(row1 - 1, col1), (row1, col1 - 1), (row1, col1 + 1), (row1 + 1, col1)]:
                        if garden[row2][col2] == plant and (row2, col2) not in reached:
                            reached.add((row2, col2))
                            queue.append((row2, col2))

                # Number of sides equals the number of corners in polygon.
                price += area * corners

    print(price)


solve("input-test-1.txt")  # 80
solve("input-test-2.txt")  # 436
solve("input-test-4.txt")  # 236
solve("input-test-5.txt")  # 368
solve("input-test-3.txt")  # 1206
solve("input.txt")  # 904114
