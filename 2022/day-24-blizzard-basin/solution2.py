from typing import Set, Tuple


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    blizzards = [line[1:-1] for line in lines[1:-1]]
    rows, cols = len(blizzards), len(blizzards[0])

    minutes = 0

    def make_trip(start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
        nonlocal minutes
        positions: Set[Tuple[int, int]] = {start_pos}

        while True:
            minutes += 1
            new_positions: Set[Tuple[int, int]] = set()

            def add_on_empty(row: int, col: int) -> None:
                if blizzards[(row + minutes) % rows][col] != '^' and \
                        blizzards[(row - minutes) % rows][col] != 'v' and \
                        blizzards[row][(col - minutes) % cols] != '>' and \
                        blizzards[row][(col + minutes) % cols] != '<':
                    new_positions.add((row, col))

            for row, col in positions:
                if (row, col) == (-1, 0):  # From top-left entry
                    new_positions.add((-1, 0))
                    add_on_empty(0, 0)
                elif (row, col) == (rows, cols - 1):  # From bottom-right entry
                    new_positions.add((rows, cols - 1))
                    add_on_empty(rows - 1, cols - 1)
                else:
                    add_on_empty(row, col)

                    if row > 0: add_on_empty(row - 1, col)  # Up
                    if row < rows - 1: add_on_empty(row + 1, col)  # Down
                    if col > 0: add_on_empty(row, col - 1)  # Left
                    if col < cols - 1: add_on_empty(row, col + 1)  # Right

                    if (row, col) == (0, 0): new_positions.add((-1, 0))  # To top-left exit
                    if (row, col) == (rows - 1, cols - 1): new_positions.add((rows, cols - 1))  # To bottom-right exit

            positions = new_positions

            if end_pos in positions:
                return

    make_trip((-1, 0), (rows, cols - 1))
    make_trip((rows, cols - 1), (-1, 0))
    make_trip((-1, 0), (rows, cols - 1))
    print(minutes)


def main():
    solve('input-test.txt')  # 54
    solve('input.txt')  # 856


if __name__ == '__main__':
    main()
