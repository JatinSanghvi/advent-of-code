def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    pos = 50
    zeroCounts = 0

    for line in lines:
        clicks = int(line[1:])

        if line[0] == "L":
            # Zero is clicked when traversing 101..200 -> 1..100 -> -99..0 -> -199..-100.
            newPos = pos - clicks
            zeroCounts += (pos - 1) // 100 - (newPos - 1) // 100
        else:
            # Zero is clicked when traversing -200..-101 -> -100..-1 -> 0..99 -> 101..199.
            newPos = pos + clicks
            zeroCounts += newPos // 100 - pos // 100

        pos = newPos % 100

    print(zeroCounts)


solve("input-test.txt")  # 6
solve("input.txt")  # 6254
