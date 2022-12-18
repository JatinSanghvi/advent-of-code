def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    cubes = [eval(line) for line in lines]

    min_x = min(x for x, y, z in cubes)
    max_x = max(x for x, y, z in cubes)
    min_y = min(y for x, y, z in cubes)
    max_y = max(y for x, y, z in cubes)
    min_z = min(z for x, y, z in cubes)
    max_z = max(z for x, y, z in cubes)

    # Air: '.', Lava: '#', Water: '~'.
    len_x, len_y, len_z = max_x - min_x + 3, max_y - min_y + 3, max_z - min_z + 3
    grid = [[['.'] * len_z for _ in range(len_y)] for _ in range(len_x)]

    for x, y, z in cubes:
        grid[x - min_x + 1][y - min_y + 1][z - min_z + 1] = '#'

    # Using breadth-first search as the depth-first search causes 'maximum recursion depth exceeded' error.
    queue = [(0, 0, 0)]
    while queue:
        x, y, z = queue.pop()
        if 0 <= x < len_x and 0 <= y < len_y and 0 <= z < len_z and grid[x][y][z] == '.':
            grid[x][y][z] = '~'
            queue.append((x - 1, y, z))
            queue.append((x + 1, y, z))
            queue.append((x, y - 1, z))
            queue.append((x, y + 1, z))
            queue.append((x, y, z - 1))
            queue.append((x, y, z + 1))

    sides = 0
    for x in range(1, len_x - 1):
        for y in range(1, len_y - 1):
            for z in range(1, len_z - 1):
                if grid[x][y][z] != '~':
                    if grid[x - 1][y][z] == '~': sides += 1
                    if grid[x + 1][y][z] == '~': sides += 1
                    if grid[x][y - 1][z] == '~': sides += 1
                    if grid[x][y + 1][z] == '~': sides += 1
                    if grid[x][y][z - 1] == '~': sides += 1
                    if grid[x][y][z + 1] == '~': sides += 1

    print(sides)


def main():
    solve('input-test.txt')  # 58
    solve('input.txt')  # 2118


if __name__ == '__main__':
    main()
