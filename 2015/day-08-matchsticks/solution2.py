def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    total = sum(line.count('\\') + line.count('"') + 2 for line in lines)
    print(total)


def main():
    solve('input-test.txt')  # 19
    solve('input.txt')  # 2046


if __name__ == '__main__':
    main()
