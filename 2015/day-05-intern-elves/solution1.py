import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    def is_nice(string):
        return len(re.findall(r'[aeiou]', string)) >= 3 and \
            re.search(r'(\w)\1', string) is not None and \
            re.search(r'ab|cd|pq|xy', string) is None

    print(sum(is_nice(line) for line in lines))


def main():
    solve('input-test1.txt')  # 2
    solve('input.txt')  # 255


if __name__ == '__main__':
    main()
