from typing import List
import re


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    # Create and populate lists for all four directions.
    size = len(lines)
    horzs: List[List[str]] = [[] for _ in range(size)]
    verts: List[List[str]] = [[] for _ in range(size)]
    rdiags: List[List[str]] = [[] for _ in range(2 * size - 1)]
    ldiags: List[List[str]] = [[] for _ in range(2 * size - 1)]

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            horzs[row].append(char)
            verts[col].append(char)
            rdiags[size + row - col - 1].append(char)
            ldiags[row + col].append(char)

    # '?=' prevents jumps to characters following the match.
    regex = re.compile(r"(?=XMAS|SAMX)")
    occurences = 0
    for lists in [horzs, verts, rdiags, ldiags]:
        occurences += sum(len(regex.findall("".join(list_))) for list_ in lists)

    print(occurences)


solve("input-test.txt")  # 18
solve("input.txt")  # 2662
