def solve(path):
    with open(path) as file:
        line = file.readline()

    floor = 0
    for index, char in enumerate(line):
        floor += 1 if char == '(' else -1
        if floor == -1:
            print(index + 1)
            return


def main():
    solve('input-test.txt')  # 1
    solve('input.txt')  # 1797


if __name__ == '__main__':
    main()
