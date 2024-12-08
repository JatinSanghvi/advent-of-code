from collections import defaultdict
from typing import Dict
import re


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    hapinesses: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for line in lines:
        match = re.match(r"^(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).$", line)
        sign = 1 if match[2] == "gain" else -1  # type: ignore
        person1, units, person2 = match[1], sign * int(match[3]), match[4]  # type: ignore
        hapinesses[person1][person2] += units
        hapinesses[person2][person1] += units

    people = list(hapinesses.keys())
    first, others = people[0], people[1:]
    size = len(others)
    max_happiness = float("-inf")

    def permute(curr=0):
        nonlocal max_happiness

        if curr == size:
            happiness = hapinesses[first][others[0]] + sum(hapinesses[others[i]][others[i + 1]] for i in range(size - 1)) + hapinesses[others[size - 1]][first]
            max_happiness = max(max_happiness, happiness)
            return

        for index in range(curr, size):
            others[curr], others[index] = others[index], others[curr]
            permute(curr + 1)
            others[curr], others[index] = others[index], others[curr]

    permute()
    print(max_happiness)


solve("input-test.txt")  # 330
solve("input.txt")  # 618
