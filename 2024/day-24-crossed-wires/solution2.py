from collections import defaultdict
from typing import Dict, List, Tuple
import re


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    values: Dict[str, int] = {}  # Wire values.

    regex = re.compile(r"(\w+): (1|0)")
    line_num = 0
    while line := lines[line_num]:
        match = regex.fullmatch(line)
        wire, value = str(match[1]), int(match[2])  # type:ignore
        values[wire] = value
        line_num += 1

    gates: Dict[str, Tuple[str, str, str]] = {}  # Gate expressions.
    dependents: Dict[str, List[str]] = defaultdict(list)  # List of dependent wires.
    dependencies: Dict[str, int] = {}  # Count of unresolved dependencies.

    regex = re.compile(r"(\w+) (\w+) (\w+) -> (\w+)")
    for line in lines[line_num + 1 :]:
        match = regex.fullmatch(line)
        input1, operation, input2, wire = str(match[1]), str(match[2]), str(match[3]), str(match[4])  # type: ignore
        gates[wire] = (input1, operation, input2)

        dependencies[wire] = 0

        if input1 not in values:
            dependents[input1].append(wire)
            dependencies[wire] += 1

        if input2 not in values:
            dependents[input2].append(wire)
            dependencies[wire] += 1

    # List of wires without unresolves dependencies.
    independents: List[str] = [wire for wire, dep in dependencies.items() if dep == 0]

    while independents:
        wire = independents.pop()
        input1, operation, input2 = gates[wire]
        if operation == "AND":
            values[wire] = values[input1] & values[input2]
        elif operation == "OR":
            values[wire] = values[input1] | values[input2]
        elif operation == "XOR":
            values[wire] = values[input1] ^ values[input2]

        for wire2 in dependents[wire]:
            dependencies[wire2] -= 1
            if dependencies[wire2] == 0:
                independents.append(wire2)

    x = y = z = 0
    for i in range(99, -1, -1):
        x = x * 2 + values.get(f"x{i:02}", 0)
        y = y * 2 + values.get(f"y{i:02}", 0)
        z = z * 2 + values.get(f"z{i:02}", 0)

    print(x + y, z)


# The input-manual file was created manually to verify the correctness of swaps.
solve("input-manual.txt")  # 44663761780968 44663761780968
