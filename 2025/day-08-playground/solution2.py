from typing import List, Tuple


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.children = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.children[px] >= self.children[py]:
            self.parent[py] = px
            self.children[px] += self.children[py]
            self.children[py] = 0
        else:
            self.parent[px] = py
            self.children[py] += self.children[px]
            self.children[px] = 0

        return True


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    coordinates = [[int(token) for token in line.split(",")] for line in lines]
    junctions = len(lines)
    distances: List[Tuple[int, int, int]] = []

    # Find distance between each pair of junctions.
    for i1 in range(junctions):
        x1, y1, z1 = coordinates[i1]
        for i2 in range(i1 + 1, junctions):
            x2, y2, z2 = coordinates[i2]
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
            distances.append((dist, i1, i2))

    distances.sort()
    uf = UnionFind(junctions)

    connects = 0
    for dist, i1, i2 in distances:
        if uf.union(i1, i2):
            connects += 1
            if connects == junctions - 1:
                break

    print(coordinates[i1][0] * coordinates[i2][0])


solve("input-test.txt")  # 25272
solve("input.txt")  # 2497445
