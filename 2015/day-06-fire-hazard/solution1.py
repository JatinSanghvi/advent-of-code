import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    grid = [[False] * 1000 for _ in range(1000)]

    for line in lines:
        match = re.match(r'^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$', line)
        instruction, x1, y1, x2, y2 = match[1], int(match[2]), int(match[3]), int(match[4]), int(match[5])

        if instruction == 'turn on':
            def value(_): return True
        elif instruction == 'turn off':
            def value(_): return False
        elif instruction == 'toggle':
            def value(cell): return not cell

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = value(grid[x][y])

    print(sum(sum(row) for row in grid))


def main():
    solve('input-test1.txt')  # 998996
    solve('input.txt')  # 543903


if __name__ == '__main__':
    main()
