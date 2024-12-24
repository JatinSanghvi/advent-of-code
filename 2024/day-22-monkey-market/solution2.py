from collections import defaultdict
from typing import Dict, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    all_changes_bananas: Dict[Tuple[int, int, int, int], int] = defaultdict(int)

    for line in lines:
        changes_bananas: Dict[Tuple[int, int, int, int], int] = {}

        last_secret = int(line)
        last_price = last_secret % 10
        d1, d2, d3 = 0, 0, 0  # Differences.

        for i in range(2000):
            secret = last_secret
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ (secret) // 32) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
            price = secret % 10
            d4 = price - last_price

            if i >= 3:
                changes_bananas.setdefault((d1, d2, d3, d4), price)

            last_secret = secret
            last_price = price
            d1, d2, d3 = d2, d3, d4

        for changes, bananas in changes_bananas.items():
            all_changes_bananas[changes] += bananas

    print(max(bananas for bananas in all_changes_bananas.values()))


solve("input-test-2.txt")  # 23
solve("input.txt")  # 1791
