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
        px = int(match.group(1))  # type: ignore
        py = int(match.group(2))  # type: ignore

        try:
            a, a_mod = divmod(px * by - py * bx, ax * by - ay * bx)
            b, b_mod = divmod(px * ay - py * ax, bx * ay - by * ax)

            if a_mod == b_mod == 0:
                tokens += 3 * a + b

        except ZeroDivisionError:
            # Find minimum value of integer 'a' for singular/impossible equations.
            # However, there were no such cases in the input data.
            print("here")
            for a in range(bx):
                b, mod = divmod(px - a * ax, bx)
                print(b, mod, bx)
                if mod == 0:
                    tokens += b
                    break

        line_num += 4

    print(tokens)


solve("input-test.txt")  # 875318608908
solve("input.txt")  # 73267584326867
