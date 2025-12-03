def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    sum = 0
    for line in lines:
        (ch1, neg_pos) = max([(ch, -pos) for (pos, ch) in enumerate(line[:-1])])
        ch2 = max([ch for ch in line[-neg_pos + 1 :]])
        sum += int(ch1 + ch2)

    print(sum)


solve("input-test.txt")  # 357
solve("input.txt")  # 17074
