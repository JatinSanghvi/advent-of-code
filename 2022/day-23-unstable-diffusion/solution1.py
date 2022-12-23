from typing import Dict, List, Set, Tuple

from collections import defaultdict


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    positions: Set[Tuple[int, int]] = {(row, col) for row, line in enumerate(lines) for col, char in enumerate(line) if char == '#'}

    # Relative positions to check, and relation position to move if the check is successful.
    checks: List[Tuple[List[Tuple[int, int]], Tuple[int, int]]] = [
        ([(-1, 0), (-1, 1), (-1, -1)], (-1, 0)),
        ([(1, 0), (1, 1), (1, -1)], (1, 0)),
        ([(0, -1), (-1, -1), (1, -1)], (0, -1)),
        ([(0, 1), (-1, 1), (1, 1)], (0, 1)),
    ]

    for round in range(10):
        new_positions: Dict[Tuple[int, int], List[Tuple[int, int]]] = defaultdict(list)

        for row, col in positions:
            if not positions.intersection([
                    (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1), (row, col + 1),
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]):
                new_pos = (row, col)
            else:
                for step in range(4):
                    dir = (round + step) % 4
                    if not any((row + row_add, col + col_add) in positions for (row_add, col_add) in checks[dir][0]):
                        new_pos = (row + checks[dir][1][0], col + checks[dir][1][1])
                        break
                else:
                    new_pos = (row, col)

            new_positions[new_pos].append((row, col))

        positions = set()
        for new_pos, old_positions in new_positions.items():
            if len(old_positions) == 1:
                positions.add(new_pos)
            else:
                positions.update(old_positions)

    row_min = min(row for row, col in positions)
    row_max = max(row for row, col in positions)
    col_min = min(col for row, col in positions)
    col_max = max(col for row, col in positions)

    print((row_max - row_min + 1) * (col_max - col_min + 1) - len(positions))


def main():
    solve('input-test.txt')  # 110
    solve('input.txt')  # 3684


if __name__ == '__main__':
    main()
