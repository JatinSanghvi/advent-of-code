from typing import Set, Tuple


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    blizzards = [line[1:-1] for line in lines[1:-1]]
    rows, cols = len(blizzards), len(blizzards[0])

    minutes = 0
    positions: Set[Tuple[int, int]] = {(-1, 0)}

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
            if (row, col) == (-1, 0):  # From entry
                new_positions.add((-1, 0))
                add_on_empty(0, 0)
            else:
                add_on_empty(row, col)  # Wait

                if row > 0: add_on_empty(row - 1, col)  # Up
                if row < rows - 1: add_on_empty(row + 1, col)  # Down
                if col > 0: add_on_empty(row, col - 1)  # Left
                if col < cols - 1: add_on_empty(row, col + 1)  # Right

                if (row, col) == (rows - 1, cols - 1):
                    new_positions.add((rows, cols - 1))  # To exit

        positions = new_positions

        if (rows, cols - 1) in positions:
            print(minutes)
            return


def main():
    solve('input-test.txt')  # 18
    solve('input.txt')  # 297


if __name__ == '__main__':
    main()
