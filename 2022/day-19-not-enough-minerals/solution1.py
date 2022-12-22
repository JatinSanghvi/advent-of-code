import re

from typing import Tuple


def get_quality(groups: Tuple[str, ...]) -> int:
    (id, ore_ore_cost, clay_ore_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost) = groups

    # Having a particular ordering of different components that make the state helps in ranking and filtering them.
    states = [(0, 0, 0, 0, 0, 0, 0, 1)]

    for _ in range(24):
        new_states = set()
        for geodes, geode_robots, obsidians, obsidian_robots, clays, clay_robots, ores, ore_robots in states:
            # No robot manufactured.
            new_states.add((geodes + geode_robots, geode_robots,
                            obsidians + obsidian_robots, obsidian_robots,
                            clays + clay_robots, clay_robots,
                            ores + ore_robots, ore_robots))

            # If ore robot is manufactured.
            if ores >= ore_ore_cost:
                new_states.add((geodes + geode_robots, geode_robots,
                                obsidians + obsidian_robots, obsidian_robots,
                                clays + clay_robots, clay_robots,
                                ores - ore_ore_cost + ore_robots, ore_robots + 1))

            # If clay robot is manufactured.
            if ores >= clay_ore_cost:
                new_states.add((geodes + geode_robots, geode_robots,
                                obsidians + obsidian_robots, obsidian_robots,
                                clays + clay_robots, clay_robots + 1,
                                ores - clay_ore_cost + ore_robots, ore_robots))

            # If obsidian robot is manufactured.
            if ores >= obsidian_ore_cost and clays >= obsidian_clay_cost:
                new_states.add((geodes + geode_robots, geode_robots,
                                obsidians + obsidian_robots, obsidian_robots + 1,
                                clays - obsidian_clay_cost + clay_robots, clay_robots,
                                ores - obsidian_ore_cost + ore_robots, ore_robots))

            # If geode robot is manufactured.
            if ores >= geode_ore_cost and obsidians >= geode_obsidian_cost:
                new_states.add((geodes + geode_robots, geode_robots + 1,
                                obsidians - geode_obsidian_cost + obsidian_robots, obsidian_robots,
                                clays + clay_robots, clay_robots,
                                ores - geode_ore_cost + ore_robots, ore_robots))

        states = sorted(new_states, reverse=True)[:1000]

    return id * states[0][0]


def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines() if line]

    pattern = re.compile(
        r'^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$')

    print(sum(get_quality(map(int, pattern.match(line).groups())) for line in lines))


def main():
    solve('input-test.txt')  # 33
    solve('input.txt')  # 1725


if __name__ == '__main__':
    main()
