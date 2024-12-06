from collections import defaultdict
from typing import Dict, List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    left_list: List[int] = []  # Left numbers.
    right_freq: Dict[int, int] = defaultdict(int)  # Right number frequencies.

    for line in lines:
        left, right = map(int, line.split("   "))
        left_list.append(left)
        right_freq[right] += 1

    similarity_score = sum(left * right_freq[left] for left in left_list)
    print(similarity_score)


def main():
    solve("input-test.txt")  # 31
    solve("input.txt")  # 26859182


if __name__ == "__main__":
    main()
