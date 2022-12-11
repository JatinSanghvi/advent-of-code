import math
from typing import Callable, List


class Monkey:
    def __init__(self, items: List[int], op: Callable[[int], int], divisor: int, next_true: int, next_false: int) -> None:
        self.items = items
        self.op = op
        self.divisor = divisor
        self.next_true = next_true
        self.next_false = next_false
        self.inspections = 0


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    monkeys: List[Monkey] = []

    for line_index in range(0, len(lines), 7):
        monkeys.append(Monkey(
            items=eval('[' + lines[line_index + 1].removeprefix('  Starting items: ') + ']'),
            op=eval('lambda old: ' + lines[line_index + 2].removeprefix('  Operation: new = ')),
            divisor=int(lines[line_index + 3].removeprefix('  Test: divisible by ')),
            next_true=int(lines[line_index + 4].removeprefix('    If true: throw to monkey ')),
            next_false=int(lines[line_index + 5].removeprefix('    If false: throw to monkey ')),
        ))

    modulo = math.prod(monkey.divisor for monkey in monkeys)

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                worry = monkey.op(item) % modulo

                if worry % monkey.divisor == 0:
                    monkeys[monkey.next_true].items.append(worry)
                else:
                    monkeys[monkey.next_false].items.append(worry)

            monkey.items = []

    inspections = sorted(monkey.inspections for monkey in monkeys)
    print(inspections[-1] * inspections[-2])


def main():
    solve('input-test.txt')  # 2713310158
    solve('input.txt')  # 12729522272


if __name__ == '__main__':
    main()
