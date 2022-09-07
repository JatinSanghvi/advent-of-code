import re


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    def is_nice(string):
        return re.search(r'(\w)(\w)\w*\1\2', string) is not None and re.search(r'(\w)\w\1', string) is not None

    print(sum(is_nice(line) for line in lines))


def main():
    solve('input-test2.txt')  # 2
    solve('input.txt')  # 55


if __name__ == '__main__':
    main()
