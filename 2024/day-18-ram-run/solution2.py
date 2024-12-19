from typing import Dict, Tuple

Item = str | Tuple[float, float]


class UnionFind:
    def __init__(self) -> None:
        self.parent: Dict[Item, Item] = {}
        self.rank: Dict[Item, int] = {}

    def find(self, x: Item) -> Item:
        self.parent.setdefault(x, x)

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x1: Item, x2: Item) -> bool:
        self.parent.setdefault(x1, x1)
        self.parent.setdefault(x2, x2)

        f1 = self.find(x1)
        f2 = self.find(x2)
        if f1 == f2:
            return False

        self.rank.setdefault(f1, 1)
        self.rank.setdefault(f2, 1)

        if self.rank[f1] >= self.rank[f2]:
            self.parent[f2] = f1
            self.rank[f1] += self.rank[f2]
        else:
            self.parent[f1] = f2
            self.rank[f2] += self.rank[f1]

        return True


def solve(path: str, size: int) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    uf = UnionFind()

    # Make two groups by connecting outer edges.
    for row in range(size):
        uf.union("top-right", (row, size - 0.5))
        uf.union("bottom-left", (row, -0.5))

    for col in range(size):
        uf.union("top-right", (-0.5, col))
        uf.union("bottom-left", (size - 0.5, col))

    # Declare the byte fallen when the two groups connect to each other.
    for line in lines:
        bx, by = eval(line)

        uf.union((bx, by), (bx - 0.5, by - 0.5))
        uf.union((bx, by), (bx - 0.5, by))
        uf.union((bx, by), (bx - 0.5, by + 0.5))
        uf.union((bx, by), (bx, by - 0.5))
        uf.union((bx, by), (bx, by + 0.5))
        uf.union((bx, by), (bx + 0.5, by - 0.5))
        uf.union((bx, by), (bx + 0.5, by))
        uf.union((bx, by), (bx + 0.5, by + 0.5))

        if uf.find("top-right") == uf.find("bottom-left"):
            print(f"{bx},{by}")
            break


solve("input-test.txt", 7)  # 6,1
solve("input.txt", 71)  # 64,54
