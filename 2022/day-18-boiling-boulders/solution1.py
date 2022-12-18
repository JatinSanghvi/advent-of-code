def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    cubes = {eval(line) for line in lines}
    sides = 0
    for x, y, z in cubes:
        if (x - 1, y, z) not in cubes: sides += 1
        if (x + 1, y, z) not in cubes: sides += 1
        if (x, y - 1, z) not in cubes: sides += 1
        if (x, y + 1, z) not in cubes: sides += 1
        if (x, y, z - 1) not in cubes: sides += 1
        if (x, y, z + 1) not in cubes: sides += 1

    print(sides)


def main():
    solve('input-test.txt')  # 64
    solve('input.txt')


if __name__ == '__main__':
    main()
