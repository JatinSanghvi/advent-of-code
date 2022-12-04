import re


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    contains_count = 0

    for line in lines:
        match = re.match(r'^(\d+)-(\d+),(\d+)-(\d+)$', line)
        [start1, stop1, start2, stop2] = map(int, [match[1], match[2], match[3], match[4]])

        if start1 <= start2 and stop1 >= stop2 or start1 >= start2 and stop1 <= stop2:
            contains_count += 1

    print(contains_count)


def main():
    solve('input-test.txt')  # 2
    solve('input.txt')  # 602


if __name__ == '__main__':
    main()
