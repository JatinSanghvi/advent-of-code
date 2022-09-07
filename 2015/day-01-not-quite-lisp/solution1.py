def solve(path):
    with open(path) as file:
        line = file.readline()

    floor = line.count('(') - line.count(')')
    print(floor)


def main():
    solve('input-test.txt')  # -3
    solve('input.txt')  # 280


if __name__ == '__main__':
    main()
