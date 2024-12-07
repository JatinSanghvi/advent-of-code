def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    predecessors = [[False] * 100 for _ in range(100)]

    # Read page ordering rules.
    num = 0
    while lines[num] != "":
        before, after = int(lines[num][:2]), int(lines[num][3:])
        predecessors[after][before] = True
        num += 1

    # Validate page orders.
    middle_sum = 0
    for line in lines[num + 1 :]:
        update = list(map(int, line.split(",")))
        size = len(update)
        ordered = True

        bi = 0
        while ordered and bi < size:
            ai = bi + 1
            while ordered and ai < size:
                if predecessors[update[bi]][update[ai]]:
                    ordered = False
                ai += 1
            bi += 1

        if ordered:
            middle_sum += update[size // 2]

    print(middle_sum)


solve("input-test.txt")  # 143
solve("input.txt")  # 4578
