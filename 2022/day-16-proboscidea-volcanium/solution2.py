import re

from typing import Dict, List, Tuple


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines() if line]

    valves: List[str] = []
    flows: Dict[str, int] = {}
    tunnels: Dict[str, List[str]] = {}

    for line in lines:
        match = re.match(r'^Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)$', line)
        valves.append(match[1])
        flows[match[1]] = int(match[2])
        tunnels[match[1]] = match[3].split(', ')

    distances: Dict[str, Dict[str, int]] = {}

    # Get minimum distance for each pair of non-empty valves.
    for from_valve in valves:
        if from_valve != 'AA' and flows[from_valve] == 0:
            continue

        distances[from_valve] = {}

        visited: List[str] = []
        visiting: List[str] = []
        to_visit = [from_valve]
        distance = 0

        while to_visit:
            visiting = to_visit
            to_visit = []
            distance += 1

            for visit_valve in visiting:
                for to_valve in tunnels[visit_valve]:
                    if to_valve not in visited and to_valve not in visiting and to_valve not in to_visit:
                        to_visit.append(to_valve)
                        if flows[to_valve] > 0:
                            distances[from_valve][to_valve] = distance

            visited += visiting

    valves = [valve for valve in valves if flows[valve] > 0]
    bits: Dict[str, int] = {valve: (1 << index) for (index, valve) in enumerate(valves)}

    def walk(from_valve: str, visited: int, minutes: int) -> int:
        if minutes <= 0:
            return 0

        if (from_valve, visited, minutes) not in cache:
            max_pressure = 0
            for to_valve in distances[from_valve]:
                if visited & bits[to_valve]:
                    continue
                remaining_minutes = minutes - distances[from_valve][to_valve] - 1
                pressure = walk(to_valve, visited | bits[to_valve], remaining_minutes) + flows[to_valve] * remaining_minutes
                max_pressure = max(max_pressure, pressure)

            cache[(from_valve, visited, minutes)] = max_pressure

        return cache[(from_valve, visited, minutes)]

    cache: Dict[Tuple[str, int, int], int] = {}

    max_pressure = 0
    max_bitmask = (1 << len(valves)) - 1
    for bitmask_1 in range(max_bitmask + 1):
        bitmask_2 = max_bitmask ^ bitmask_1
        max_pressure = max(max_pressure, walk('AA', bitmask_1, 26) + walk('AA', bitmask_2, 26))

    print(max_pressure)


def main():
    solve('input-test.txt')  # 1707
    solve('input.txt')  # 2594


if __name__ == '__main__':
    main()
