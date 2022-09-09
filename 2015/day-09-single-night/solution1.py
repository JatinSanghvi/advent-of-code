import re


def solve(path):
    with open(path) as file:
        lines = file.read().splitlines()

    locations = set()
    distances = {}

    for line in lines:
        match = re.match(r'^(\w+) to (\w+) = (\d+)$', line)
        location1, location2, distance = match[1], match[2], int(match[3])
        locations.add(location1)
        locations.add(location2)
        distances[(location1, location2)] = distance
        distances[(location2, location1)] = distance

    for location in locations:
        distances[(None, location)] = 0

    def longest_distance(locations, source_location, prev_distance):
        if len(locations) == 1:
            return prev_distance

        new_locations = locations - {source_location}
        return min(longest_distance(new_locations, location, prev_distance + distances[source_location, location]) for location in new_locations)

    print(longest_distance(locations, None, 0))


def main():
    solve('input-test.txt')  # 605
    solve('input.txt')  # 251


if __name__ == '__main__':
    main()
