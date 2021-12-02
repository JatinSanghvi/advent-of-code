with open("input.txt") as file:
    list = [int(line) for line in file.readlines()]

print(sum(list[index] > list[index - 1] for index in range(1, len(list))))
