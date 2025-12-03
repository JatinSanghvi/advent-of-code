def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    line_len = len(lines[0])
    sum = 0
    for line in lines:
        num = ""
        pos = -1
        for digit in range(12):
            (ch, neg_pos) = max([(ch, -pos) for (pos, ch) in enumerate(line[pos + 1 : line_len - 11 + digit])])
            pos += -neg_pos + 1  # Convert relative index to absolute index.
            num += ch
        sum += int(num)

    print(sum)


solve("input-test.txt")  # 3121910778619
solve("input.txt")  # 169512729575727
