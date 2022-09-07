def solve(path):
    with open(path) as file:
        line = file.readline()

    pos, other_pos = (0, 0), (0, 0)
    positions = {pos}

    for char in line:
        pos, other_pos = other_pos, pos

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
    solve('input-test1.txt')  # 3
    solve('input-test2.txt')  # 11
    solve('input.txt')  # 2631


if __name__ == '__main__':
    main()
