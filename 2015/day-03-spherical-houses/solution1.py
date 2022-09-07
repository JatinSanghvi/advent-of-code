def solve(path):
    with open(path) as file:
        line = file.readline()

    pos = (0, 0)
    positions = {pos}

    for char in line:
        if char == '^':
            pos = (pos[0], pos[1] - 1)
        elif char == 'v':
            pos = (pos[0], pos[1] + 1)
        elif char == '>':
            pos = (pos[0] + 1, pos[1])
        elif char == '<':
            pos = (pos[0] - 1, pos[1])

        positions.add(pos)

    print(len(positions))


def main():
    solve('input-test1.txt')  # 4
    solve('input-test2.txt')  # 2
    solve('input.txt')  # 2572


if __name__ == '__main__':
    main()
