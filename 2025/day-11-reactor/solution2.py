import functools
from typing import Dict, List, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    graph: Dict[str, List[str]] = {}
    for line in lines:
        from_str, *to_strs = line.split(" ")
        graph[from_str[:-1]] = to_strs

    # Returns count of paths in format (none, has-dac, has-fft, has-both).
    @functools.cache
    def paths(device: str) -> Tuple[int, int, int, int]:
        if device == "out":
            return (1, 0, 0, 0)
        else:
            sum_paths = [sum(items) for items in zip(*map(paths, graph[device]))]
            if device == "dac":
                sum_paths[1] += sum_paths[0]
                sum_paths[3] += sum_paths[2]
            elif device == "fft":
                sum_paths[2] += sum_paths[0]
                sum_paths[3] += sum_paths[1]
            return tuple(sum_paths)

    print(paths("svr")[3])


solve("input-test2.txt")  # 2
solve("input.txt")  # 466
