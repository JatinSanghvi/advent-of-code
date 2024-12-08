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
    size = len(people)
    max_happiness = float("-inf")

    def permute(curr=0):
        nonlocal max_happiness

        if curr == size:
            happiness = sum(hapinesses[people[i]][people[i + 1]] for i in range(size - 1))
            max_happiness = max(max_happiness, happiness)
            return

        for index in range(curr, size):
            people[curr], people[index] = people[index], people[curr]
            permute(curr + 1)
            people[curr], people[index] = people[index], people[curr]

    permute()
    print(max_happiness)


solve("input-test.txt")  # 286
solve("input.txt")  # 601
