from typing import Dict, Set


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

    middle_sum = 0
    for line in lines[num + 1 :]:
        update = list(map(int, line.split(",")))
        size = len(update)

        # Check page order.
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
            continue

        # Create dependency graph to orrect page order.
        followers: Dict[int, Set[int]] = {page: set() for page in update}
        pred_counts: Dict[int, int] = {page: 0 for page in update}

        for page1 in update:
            for page2 in update:
                if predecessors[page1][page2]:
                    followers[page2].add(page1)
                    pred_counts[page1] += 1

        # Get `size // 2`-th element in the topological sort order.
        rank = 0
        page1 = next(page for page, count in pred_counts.items() if count == 0)
        while rank < size // 2:
            for page2 in followers[page1]:
                pred_counts[page2] -= 1
                if pred_counts[page2] == 0:
                    page1 = page2
            rank += 1

        middle_sum += page1

    print(middle_sum)


solve("input-test.txt")  # 123
solve("input.txt")  # 6179
