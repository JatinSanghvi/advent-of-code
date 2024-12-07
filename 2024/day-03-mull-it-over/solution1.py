import re


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    # Find all occurences of expression `mul(a,b)`.
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    result = 0
    for exp in regex.finditer(text):
        result += int(exp.group(1)) * int(exp.group(2))

    print(result)


solve("input-test-1.txt")  # 161
solve("input.txt")  # 179571322
