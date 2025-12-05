def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    divider = lines.index("")
    ranges = sorted([tuple(int(val) for val in line.split("-")) for line in lines[:divider]])

    ids = 0
    prev_max = 0
    for min, max_ in ranges:
        if prev_max < max_:
            ids += max_ - max(prev_max, min - 1)
            prev_max = max_

    print(ids)


solve("input-test.txt")  # 14
solve("input.txt")  # 358155203664116
