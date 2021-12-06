def solve(path):
    with open(path) as file:
        line = file.readline()

    days = 256
    timers = [int(timer) for timer in line.split(",")]

    # Number of Lanternfishes with given age on final day.
    max_age = days + 8
    fishes = [0] * (max_age + 1)

    for timer in timers:
        fishes[max_age - timer] += 1

    for age in range(max_age, -1, -1):
        for child_age in range(age - 9, -1, -7):
            fishes[child_age] += fishes[age]

    print(sum(fishes))

solve("input-test.txt")
solve("input.txt")
