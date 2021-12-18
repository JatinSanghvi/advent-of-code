import functools


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value}'"


def create_tree(snailfish):
    prev = None

    def create_tree_internal(snailfish):
        nonlocal prev
        if type(snailfish) is int:
            curr = Node(snailfish, prev, None)
            if prev != None: prev.right = curr
            prev = curr
            return curr
        return [create_tree_internal(snailfish[0]), create_tree_internal(snailfish[1])]
    return create_tree_internal(snailfish)


def create_snailfish(tree):
    if type(tree) is Node:
        return tree.value
    else:
        return [create_snailfish(tree[0]), create_snailfish(tree[1])]


def explode(tree):
    def explode_internal(tree, depth):
        if depth == 4 and type(tree[0]) is Node and type(tree[1]) is Node:
            new_node = Node(0, tree[0].left, tree[1].right)
            if tree[0].left != None: tree[0].left.value += tree[0].value; tree[0].left.right = new_node
            if tree[1].right != None: tree[1].right.value += tree[1].value; tree[1].right.left = new_node
            return True, new_node
        else:
            is_exploded = False
            if not is_exploded and type(tree[0]) is not Node:
                (is_exploded, tree[0]) = explode_internal(tree[0], depth + 1)
            if not is_exploded and type(tree[1]) is not Node:
                (is_exploded, tree[1]) = explode_internal(tree[1], depth + 1)
            return is_exploded, tree

    return explode_internal(tree, 0)


def split(tree):
    def split_internal(tree):
        if type(tree) is Node:
            if tree.value < 10:
                return False, tree
            else:
                new_tree = [Node(tree.value // 2, tree.left, None),
                            Node(tree.value - tree.value // 2, None, tree.right)]
                new_tree[1].left = new_tree[0]
                new_tree[0].right = new_tree[1]
                if tree.left != None: tree.left.right = new_tree[0]
                if tree.right != None: tree.right.left = new_tree[1]
                return True, new_tree
        else:
            is_splitted = False
            if not is_splitted: (is_splitted, tree[0]) = split_internal(tree[0])
            if not is_splitted: (is_splitted, tree[1]) = split_internal(tree[1])
            return is_splitted, tree

    return split_internal(tree)


def reduce(snailfish):
    tree = create_tree(snailfish)

    is_updated = True
    while is_updated:
        is_updated = False
        if not is_updated: (is_updated, tree) = explode(tree)
        if not is_updated: (is_updated, tree) = split(tree)

    return create_snailfish(tree)


def add(snailfish1, snailfish2):
    return reduce([snailfish1, snailfish2])


def sum(snailfishes):
    return functools.reduce(lambda s1, s2: add(s1, s2), snailfishes)


def magnitude(snailfish):
    if type(snailfish) is int:
        return snailfish
    else:
        return 3 * magnitude(snailfish[0]) + 2 * magnitude(snailfish[1])


assert reduce([[[[[9, 8], 1], 2], 3], 4]) == [[[[0, 9], 2], 3], 4]
assert reduce([7, [6, [5, [4, [3, 2]]]]]) == [7, [6, [5, [7, 0]]]]
assert reduce([[6, [5, [4, [3, 2]]]], 1]) == [[6, [5, [7, 0]]], 3]
assert reduce([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]) == [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
assert reduce([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]) == [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]

assert reduce([10, 0]) == [[5, 5], 0]
assert reduce([11, 0]) == [[5, 6], 0]
assert reduce([12, 0]) == [[6, 6], 0]

assert add([[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]) == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

assert sum([[1, 1], [2, 2], [3, 3], [4, 4]]) == [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]
assert sum([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]
assert sum([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]

assert sum([
    [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
    [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
    [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
    [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
    [7, [5, [[3, 8], [1, 4]]]],
    [[2, [2, 2]], [8, [8, 1]]],
    [2, 9],
    [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
    [[[5, [7, 4]], 7], 1],
    [[[[4, 2], 2], 6], [8, 7]]
]) == [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]

assert magnitude([[1, 2], [[3, 4], 5]]) == 143
assert magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]) == 1384
assert magnitude([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]) == 445
assert magnitude([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]) == 791
assert magnitude([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]) == 1137
assert magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]) == 3488


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    print(magnitude(sum([eval(line) for line in lines])))


solve("input-test.txt")
solve("input.txt")
