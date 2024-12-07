def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Search for all X-shapes of MAS.
    occurences = 0
    size = len(lines)
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            if (
                lines[r][c] == "A"
                and (lines[r - 1][c - 1] == "M" and lines[r + 1][c + 1] == "S" or lines[r - 1][c - 1] == "S" and lines[r + 1][c + 1] == "M")
                and (lines[r - 1][c + 1] == "M" and lines[r + 1][c - 1] == "S" or lines[r - 1][c + 1] == "S" and lines[r + 1][c - 1] == "M")
            ):
                occurences += 1

    print(occurences)


solve("input-test.txt")  # 9
solve("input.txt")  # 2034
