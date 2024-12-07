from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Compose left and right lists.
    left_list: List[int] = []
    right_list: List[int] = []

    for line in lines:
        left, right = map(int, line.split("   "))
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    # Find distance between list elements in sorted list.
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    print(total_distance)


solve("input-test.txt")  # 11
solve("input.txt")  # 1320851
