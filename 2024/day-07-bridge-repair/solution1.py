def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    total = 0
    for line in lines:
        result = int(line.split(": ")[0])
        operands = list(map(int, line.split(": ")[1].split(" ")))

        results = set([operands[0]])
        for op in operands[1:]:
            new_results = set()
            for res in results:
                new_results.add(res + op)
                new_results.add(res * op)
            results = new_results

        if result in results:
            total += result

    print(total)


solve("input-test.txt")  # 3749
solve("input.txt")  # 1153997401072
