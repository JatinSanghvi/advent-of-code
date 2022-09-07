def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    total = sum(len(line) - len(eval(line)) for line in lines)
    print(total)


def main():
    solve('input-test.txt')  # 12
    solve('input.txt')  # 1333


if __name__ == '__main__':
    main()
