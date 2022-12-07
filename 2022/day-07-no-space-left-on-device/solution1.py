from typing import List, NewType, Union

Tree = NewType('Tree', List[Union['Tree', int]])


def solve(path):
    def add_children(tree: Tree) -> Tree:
        while (line := file.readline()) not in ['$ cd ..\n', '']:
            if line.startswith('$ cd '):
                tree.append(add_children([]))
            elif line.startswith('$ ') or line.startswith('dir '):
                pass
            else:
                tree.append(int(line.split(' ')[0]))

        return tree

    with open(path) as file:
        root = add_children([])

    def walk(tree: Tree) -> int:
        nonlocal total_size
        dir_size = sum(item if type(item) is int else walk(item) for item in tree)
        if dir_size <= 100000:
            total_size += dir_size
        return dir_size

    total_size = 0
    walk(root)

    print(total_size)


def main():
    solve('input-test.txt')  # 95437
    solve('input.txt')  # 1306611


if __name__ == '__main__':
    main()
