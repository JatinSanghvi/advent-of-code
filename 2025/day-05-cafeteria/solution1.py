def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    divider = lines.index("")
    ranges = [[int(val) for val in line.split("-")] for line in lines[:divider]]

    fresh = 0
    for line in lines[divider + 1 :]:
        id = int(line)
        for min, max in ranges:
            if min <= id <= max:
                fresh += 1
                break

    print(fresh)


solve("input-test.txt")  # 3
solve("input.txt")  # 679
