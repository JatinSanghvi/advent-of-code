import re


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    regex = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")

    result = 0
    do = True

    for exp in regex.finditer(text):
        token = exp.group(0)
        if token == "do()":
            do = True
        elif token == "don't()":
            do = False
        elif do:
            result += int(exp.group(1)) * int(exp.group(2))

    print(result)


def main():
    solve("input-test-2.txt")  # 48
    solve("input.txt")  # 103811193


if __name__ == "__main__":
    main()
