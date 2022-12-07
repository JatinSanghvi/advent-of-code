from typing import List, NewType, Union

Tree = NewType('Tree', List[Union['Tree', int]])


def solve(path):
    def add_children(tree: Tree) -> Tree:
        nonlocal used_space
        while (line := file.readline()) not in ['$ cd ..\n', '']:
            if line.startswith('$ cd '):
                tree.append(add_children([]))
            elif line.startswith('$ ') or line.startswith('dir '):
                pass
            else:
                file_size = int(line.split(' ')[0])
                tree.append(file_size)
                used_space += file_size

        return tree

    used_space = 0
    with open(path) as file:
        root = add_children([])

    free_space = 70_000_000 - used_space
    req_space = 30_000_000 - free_space

    def walk(tree: Tree) -> int:
        nonlocal smallest_dir_size
        dir_size = sum(item if type(item) is int else walk(item) for item in tree)
        if smallest_dir_size > dir_size >= req_space:
            smallest_dir_size = dir_size
        return dir_size

    smallest_dir_size = 70_000_000
    walk(root)

    print(smallest_dir_size)


def main():
    solve('input-test.txt')  # 24933642
    solve('input.txt')  # 1306611


if __name__ == '__main__':
    main()
