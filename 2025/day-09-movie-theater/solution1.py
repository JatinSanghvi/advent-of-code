def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    points = [tuple(map(int, line.split(","))) for line in lines]

    max_area = 0
    for i1 in range(len(points)):
        x1, y1 = points[i1]
        for i2 in range(i1 + 1, len(points)):
            x2, y2 = points[i2]
            area = (max(x1, x2) - min(x1, x2) + 1) * (max(y1, y2) - min(y1, y2) + 1)
            max_area = max(max_area, area)

    print(max_area)


solve("input-test.txt")  # 50
solve("input.txt")  # 4777824480
