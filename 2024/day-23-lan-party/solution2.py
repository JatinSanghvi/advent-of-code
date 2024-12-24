from typing import List, Set, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    computers: Set[str] = set()
    connections: Set[Tuple[str, str]] = set()
    for line in lines:
        comp1, comp2 = line[0:2], line[3:5]
        computers.update([comp1, comp2])
        connections.add((min(comp1, comp2), max(comp1, comp2)))

    comp_sets = [[comp1, comp2] for comp1, comp2 in connections]
    while len(comp_sets) > 1:
        new_comp_sets: List[List[str]] = []
        for comp_set in comp_sets:
            for comp2 in computers:
                if all((comp1, comp2) in connections for comp1 in comp_set):
                    new_comp_sets.append(comp_set + [comp2])
        comp_sets = new_comp_sets

    print(",".join(comp_sets[0]))


solve("input-test.txt")  # co,de,ka,ta
solve("input.txt")  # ag,gh,hh,iv,jx,nq,oc,qm,rb,sm,vm,wu,zr
