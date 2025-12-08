from typing import List, Tuple


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.circuit_len = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.circuit_len[px] >= self.circuit_len[py]:
                self.parent[py] = px
                self.circuit_len[px] += self.circuit_len[py]
                self.circuit_len[py] = 0
            else:
                self.parent[px] = py
                self.circuit_len[py] += self.circuit_len[px]
                self.circuit_len[px] = 0


def solve(path: str, connects: int) -> None:
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

    for i in range(connects):
        dist, i1, i2 = distances[i]
        uf.union(i1, i2)

    uf.circuit_len.sort()
    print(uf.circuit_len[-1] * uf.circuit_len[-2] * uf.circuit_len[-3])


solve("input-test.txt", 10)  # 40
solve("input.txt", 1000)  # 131150
