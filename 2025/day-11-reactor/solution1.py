import functools
from typing import Dict, List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    graph: Dict[str, List[str]] = {}
    for line in lines:
        from_str, *to_strs = line.split(" ")
        graph[from_str[:-1]] = to_strs

    @functools.cache
    def paths(device: str) -> int:
        return 1 if device == "out" else sum(map(paths, graph[device]))

    print(paths("you"))


solve("input-test1.txt")  # 5
solve("input.txt")  # 466
