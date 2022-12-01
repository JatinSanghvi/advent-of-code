def solve(path):
    with open(path) as file:
        lines = [''] + [line.rstrip() for line in file.readlines()]

    all_calories = []

    for line in lines:
        if line == '':
            all_calories.append(0)
        else:
            all_calories[-1] += int(line)

    print(sum(sorted(all_calories)[-3:]))


def main():
    solve('input-test.txt')  # 45000
    solve('input.txt')  # 199357


if __name__ == '__main__':
    main()
