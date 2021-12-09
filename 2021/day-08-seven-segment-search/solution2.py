def solve(path):
    with open(path) as file:
        lines = file.readlines()

    sum = 0
    for line in lines:
        [displays, digits] = [[set(segments) for segments in split.split()] for split in line.split(" | ")]

        list = [None] * 10
        list[1] = next(d for d in displays if len(d) == 2)
        list[4] = next(d for d in displays if len(d) == 4)
        list[7] = next(d for d in displays if len(d) == 3)
        list[8] = next(d for d in displays if len(d) == 7)
        list[9] = next(d for d in displays if len(d) == 6 and set(list[4]) < set(d))
        list[6] = next(d for d in displays if len(d) == 6 and not set(list[7]) < set(d))
        list[0] = next(d for d in displays if len(d) == 6 and not set(list[4]) < set(d) and set(list[7]) < set(d))
        list[3] = next(d for d in displays if len(d) == 5 and set(list[7]) < set(d))
        list[5] = next(d for d in displays if len(d) == 5 and set(d) < set(list[6]))
        list[2] = next(d for d in displays if len(d) == 5 and not set(d) < set(list[9]))

        number = "".join(str(list.index(d)) for d in digits)
        sum += int(number)

    print(sum)


solve("input-test.txt")
solve("input.txt")
