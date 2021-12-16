from collections import defaultdict


class Graph(object):
    """ Graph data structure, source: https://stackoverflow.com/a/30747003 """

    def __init__(self, edges):
        self._graph = defaultdict(set)

        for node1, node2 in edges:
            self._graph[node1].add(node2)
            self._graph[node2].add(node1)

    def count_paths(self, node="start", path=[], visited_twice=False):
        if node == "end": return 1
        if node.islower(): path = path + [node]

        count = 0
        for node2 in self._graph[node]:
            if node2 not in path:
                count += self.count_paths(node2, path, visited_twice)
            elif node2 != "start" and not visited_twice:
                count += self.count_paths(node2, path, True)

        return count

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    edges = [tuple(line.rstrip().split("-")) for line in lines]
    graph = Graph(edges)
    print(graph.count_paths())


solve("input-test-1.txt")
solve("input-test-2.txt")
solve("input-test-3.txt")
solve("input.txt")
