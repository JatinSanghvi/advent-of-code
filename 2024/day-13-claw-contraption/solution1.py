import re


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    tokens = 0

    line_num = 0
    while line_num < len(lines):
        match = re.fullmatch(r"Button A: X\+(\d+), Y\+(\d+)", lines[line_num])
        ax, ay = int(match.group(1)), int(match.group(2))  # type: ignore

        match = re.fullmatch(r"Button B: X\+(\d+), Y\+(\d+)", lines[line_num + 1])
        bx, by = int(match.group(1)), int(match.group(2))  # type: ignore

        match = re.fullmatch(r"Prize: X=(\d+), Y=(\d+)", lines[line_num + 2])
        px, py = int(match.group(1)), int(match.group(2))  # type: ignore

        for a in range(101):
            b1, mod1 = divmod(px - a * ax, bx)
            b2, mod2 = divmod(py - a * ay, by)

            if mod1 == mod2 == 0 and b1 == b2 >= 0:
                tokens += 3 * a + b1
                break

        line_num += 4

    print(tokens)


solve("input-test.txt")  # 480
solve("input.txt")  # 39996
