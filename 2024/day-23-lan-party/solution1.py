from collections import defaultdict
from typing import Dict, Set


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    connections: Dict[str, Set[str]] = defaultdict(set)
    for line in lines:
        comp1, comp2 = line[0:2], line[3:5]
        connections[min(comp1, comp2)].add(max(comp1, comp2))

    num_sets = 0
    for comp1, comp_set in connections.items():
        comps = list(sorted(comp_set))
        for comp2 in comps:
            for comp3 in comps:
                if comp2 in connections and comp3 in connections[comp2] and (comp1[0] == "t" or comp2[0] == "t" or comp3[0] == "t"):
                    num_sets += 1

    print(num_sets)


solve("input-test.txt")  # 7
solve("input.txt")  # 1200
