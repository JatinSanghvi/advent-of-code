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

    for round in range(10000):
        new_positions: Dict[Tuple[int, int], List[Tuple[int, int]]] = defaultdict(list)
        moved = False

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
                        moved = True
                        break
                else:
                    new_pos = (row, col)

            new_positions[new_pos].append((row, col))

        if not moved: break

        positions = set()
        for new_pos, old_positions in new_positions.items():
            if len(old_positions) == 1:
                positions.add(new_pos)
            else:
                positions.update(old_positions)

    print(round + 1)


def main():
    solve('input-test.txt')  # 20
    solve('input.txt')  # 862


if __name__ == '__main__':
    main()
