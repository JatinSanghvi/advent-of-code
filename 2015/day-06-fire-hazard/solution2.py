import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    grid = [[0] * 1000 for _ in range(1000)]

    for line in lines:
        match = re.match(r'^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$', line)
        instruction, x1, y1, x2, y2 = match[1], int(match[2]), int(match[3]), int(match[4]), int(match[5])

        if instruction == 'turn on':
            def value(brightness): return brightness + 1
        elif instruction == 'turn off':
            def value(brightness): return max(0, brightness - 1)
        elif instruction == 'toggle':
            def value(brightness): return brightness + 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = value(grid[x][y])

    print(sum(sum(row) for row in grid))


def main():
    solve('input-test2.txt')  # 2000001
    solve('input.txt')  # 14687245


if __name__ == '__main__':
    main()
