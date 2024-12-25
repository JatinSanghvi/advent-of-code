from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    locks: List[List[int]] = []
    keys: List[List[int]] = []

    for line_num in range(0, len(lines), 8):
        tools = locks if lines[line_num][0] == "#" else keys
        heights = [sum(line[pin] == "#" for line in lines[line_num + 1 : line_num + 6]) for pin in range(5)]
        tools.append(heights)

    pairs = sum(all(lpin + kpin <= 5 for lpin, kpin in zip(lock, key)) for lock in locks for key in keys)
    print(pairs)


solve("input-test.txt")  # 3
solve("input.txt")  # 3127
