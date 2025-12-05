def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    rows = len(lines)
    cols = len(lines[0])

    accessible = 0
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "@":
                neighbors = 0
                for r2 in range(max(0, r - 1), min(rows, r + 2)):
                    for c2 in range(max(0, c - 1), min(cols, c + 2)):
                        if lines[r2][c2] == "@":
                            neighbors += 1

                if neighbors <= 4:
                    accessible += 1

    print(accessible)


solve("input-test.txt")  # 13
solve("input.txt")  # 1518
