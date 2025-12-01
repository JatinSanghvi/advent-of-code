def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    pos = 50
    zeroCounts = 0

    for line in lines:
        clicks = int(line[1:])
        if line[0] == "L":
            pos = (pos - clicks) % 100
        else:
            pos = (pos + clicks) % 100

        if pos == 0:
            zeroCounts += 1

    print(zeroCounts)


solve("input-test.txt")  # 3
solve("input.txt")  # 1074
