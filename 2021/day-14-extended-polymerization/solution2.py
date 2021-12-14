from collections import defaultdict


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    template = lines[0]
    next_pairs = {}
    for line in lines[2:]:
        splits = line.split()
        next_pairs[splits[0]] = (splits[0][0] + splits[2], splits[2] + splits[0][1])

    pair_counts = {pair: 0 for pair in next_pairs.keys()}
    for index in range(len(template) - 1):
        pair_counts[template[index] + template[index + 1]] += 1

    steps = 40

    for _ in range(steps):
        new_pair_counts = {pair: 0 for pair in next_pairs.keys()}
        for pair, count in pair_counts.items():
            new_pairs = next_pairs[pair]
            new_pair_counts[new_pairs[0]] += count
            new_pair_counts[new_pairs[1]] += count

        pair_counts = new_pair_counts

    element_counts = defaultdict(lambda: 0)
    element_counts[template[0]] += 1
    element_counts[template[-1]] += 1
    for pair, count in pair_counts.items():
        element_counts[pair[0]] += count
        element_counts[pair[1]] += count

    counts = [count // 2 for count in element_counts.values()]
    print(max(counts) - min(counts))


solve("input-test.txt")
solve("input.txt")
