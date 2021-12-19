transformations = [
    (-1, 0, -1, 1, 1, 2),
    (-1, 0, -1, 2, -1, 1),
    (-1, 0, 1, 1, -1, 2),
    (-1, 0, 1, 2, 1, 1),
    (-1, 1, -1, 0, -1, 2),
    (-1, 1, -1, 2, 1, 0),
    (-1, 1, 1, 0, 1, 2),
    (-1, 1, 1, 2, -1, 0),
    (-1, 2, -1, 0, 1, 1),
    (-1, 2, -1, 1, -1, 0),
    (-1, 2, 1, 0, -1, 1),
    (-1, 2, 1, 1, 1, 0),
    (1, 0, -1, 1, -1, 2),
    (1, 0, -1, 2, 1, 1),
    (1, 0, 1, 1, 1, 2),
    (1, 0, 1, 2, -1, 1),
    (1, 1, -1, 0, 1, 2),
    (1, 1, -1, 2, -1, 0),
    (1, 1, 1, 0, -1, 2),
    (1, 1, 1, 2, 1, 0),
    (1, 2, -1, 0, -1, 1),
    (1, 2, -1, 1, 1, 0),
    (1, 2, 1, 0, 1, 1),
    (1, 2, 1, 1, -1, 0),
]


def transform(tran, pos):
    return (tran[0] * pos[tran[1]], tran[2] * pos[tran[3]], tran[4] * pos[tran[5]])


def translate(tran, pos):
    return (pos[0] + tran[0], pos[1] + tran[1], pos[2] + tran[2])


def get_translation(pos1, pos2):
    return (pos2[0] - pos1[0], pos2[1] - pos1[1], pos2[2] - pos1[2])


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    split_pos = [index for index, line in enumerate(lines) if line == "\n"]
    all_scanner_pos = [lines[start + 2:end] for start, end in zip([-1] + split_pos, split_pos + [None])]
    all_scanner_pos = [[tuple(int(coor) for coor in pos.split(",")) for pos in scanner_pos] for scanner_pos in all_scanner_pos]

    scanner_pairs = []

    for index1, s1_pos in enumerate(all_scanner_pos):
        s1_pos_set = set(s1_pos)
        for index2, s2_pos in enumerate(all_scanner_pos):
            if index2 == index1: continue
            break_out = False
            for transformation in transformations:
                s2_pos_transformed = [transform(transformation, pos) for pos in s2_pos]
                for pos2 in s2_pos_transformed[11:]:  # Optimization
                    for pos1 in s1_pos_set:
                        translation = get_translation(pos2, pos1)
                        s2_pos_set = set(translate(translation, pos) for pos in s2_pos_transformed)
                        intersections = len(s1_pos_set.intersection(s2_pos_set))
                        if (intersections >= 12):
                            scanner_pairs.append((index1, index2, transformation, translation))
                            break_out = True
                            break
                    if break_out: break
                if break_out: break

    queue = [0]
    ordered_pairs = []
    for index in range(len(all_scanner_pos)):
        for pair in scanner_pairs:
            if pair[0] == queue[index] and pair[1] not in queue:
                queue.append(pair[1])
                ordered_pairs.append(pair)

    groups = [set(scanner_pos) for scanner_pos in all_scanner_pos]
    for ordered_pair in reversed(ordered_pairs):
        transformed = [transform(ordered_pair[2], pos) for pos in groups[ordered_pair[1]]]
        translated = [translate(ordered_pair[3], pos) for pos in transformed]
        groups[ordered_pair[0]] = groups[ordered_pair[0]].union(set(translated))

    print(len(groups[0]))


solve("input-test.txt")
solve("input.txt")
