from typing import List

import re


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    divider_index = lines.index('')
    line_width = len(lines[divider_index - 1])
    stacks: List[List[str]] = []

    for char_index in range(1, line_width, 4):
        stacks.append([line[char_index] for line in lines[divider_index - 2::-1] if line[char_index] != ' '])

    for line in lines[divider_index + 1:]:
        match = re.match(r'^move (\d+) from (\d+) to (\d+)$', line)
        [num_crates, from_index, to_index] = map(int, [match[1], match[2], match[3]])

        for _ in range(num_crates):
            stacks[to_index - 1].append(stacks[from_index - 1].pop())

    print(''.join([stack[-1] if len(stack) else '' for stack in stacks]))


def main():
    solve('input-test.txt')  # CMZ
    solve('input.txt')  # TQRFCBSJJ


if __name__ == '__main__':
    main()
