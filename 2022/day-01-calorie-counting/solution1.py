def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()] + ['']

    max_calories = 0
    curr_calories = 0

    for line in lines:
        if line == '':
            if max_calories < curr_calories:
                max_calories = curr_calories
            curr_calories = 0
        else:
            curr_calories += int(line)

    print(max_calories)


def main():
    solve('input-test.txt')  # 24000
    solve('input.txt')  # 67450


if __name__ == '__main__':
    main()
