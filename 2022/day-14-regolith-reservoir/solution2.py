from typing import List, Tuple


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines() if line]

    rocks: List[List[Tuple[int, int]]] = []
    for line in lines:
        rocks.append(([tuple(map(int, pos.split(','))) for pos in line.split(' -> ')]))

    # Add vertical space to fit in the floor.
    max_y = max(max(pos[1] for pos in rock) for rock in rocks) + 2

    # Add horizontal space to allow the sand to drop to maximum distance, plus one more on both sides to have a floor of
    # sufficient length so that the falling sand can find rocks on either side.
    min_x = min(min(min(pos[0] for pos in rock) for rock in rocks), 500 - max_y)
    max_x = max(max(max(pos[0] for pos in rock) for rock in rocks), 500 + max_y)

    # min_x is the x-coordinate that should be positioned at index 0.
    diff_x = min_x

    # Normalize the coordinates based on the range.
    rocks = [[(x - diff_x, y) for x, y in rock] for rock in rocks]

    grid = [(max_x - min_x + 1) * ['.'] for _ in range(max_y + 1)]

    # Fill the grid with rocks.
    for rock in rocks:
        x, y = rock[0]
        grid[y][x] = '#'

        for x2, y2 in rock[1:]:
            while x != x2 or y != y2:
                if x < x2: x += 1
                elif x > x2: x -= 1
                elif y < y2: y += 1
                elif y > y2: y -= 1
                grid[y][x] = '#'

    # Fill the floor with rocks.
    for x in range(max_x - min_x + 1):
        grid[max_y][x] = '#'

    sand_start = (500 - diff_x, 0)

    num_sand = 0
    x, y = sand_start

    # Drop a sand unit. Each iteration represents a clock cycle.
    while grid[y][x] != 'o':
        if grid[y + 1][x] == '.':
            y += 1
        elif grid[y + 1][x - 1] == '.':
            y += 1
            x -= 1
        elif grid[y + 1][x + 1] == '.':
            y += 1
            x += 1
        else:
            # Settle the sand unit, and create a new one.
            grid[y][x] = 'o'
            num_sand += 1
            x, y = sand_start

    # for row in grid:
    #     print(''.join(row))

    print(num_sand)
    return


def main():
    solve('input-test.txt')  # 93
    solve('input.txt')  # 25161


if __name__ == '__main__':
    main()
