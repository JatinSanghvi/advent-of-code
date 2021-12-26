def print_map(map):
    print('[')
    for row in map:
        print(f'\t{"".join(row)}')
    print(']')


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    map = [[loc for loc in line.rstrip()] for line in lines]
    rows = len(map)
    columns = len(map[0])

    for step in range(1000):
        map1 = [['>' if map[row][col] == '.' and map[row][(col - 1) % columns] == '>' else
                 '.' if map[row][col] == '>' and map[row][(col + 1) % columns] == '.' else
                 map[row][col]
                 for col in range(columns)] for row in range(rows)]

        map2 = [['v' if map1[row][col] == '.' and map1[(row - 1) % rows][col] == 'v' else
                 '.' if map1[row][col] == 'v' and map1[(row + 1) % rows][col] == '.' else
                 map1[row][col]
                 for col in range(columns)] for row in range(rows)]

        if (map == map2): break
        map = map2

    print(step + 1)


solve('input-test.txt')
solve('input.txt')
