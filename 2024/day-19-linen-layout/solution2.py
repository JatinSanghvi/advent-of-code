def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    towels = set(lines[0].split(", "))
    max_len = max(len(towel) for towel in towels)
    count = 0

    for design in lines[2:]:
        counts = [1] + [0] * len(design)
        for pos in range(1, len(design) + 1):
            for start_pos in range(max(0, pos - max_len), pos):
                if design[start_pos:pos] in towels:
                    counts[pos] += counts[start_pos]

        count += counts[-1]

    print(count)


solve("input-test.txt")  # 16
solve("input.txt")  # 577474410989846