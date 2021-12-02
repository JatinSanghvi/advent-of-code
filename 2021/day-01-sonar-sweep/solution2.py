with open("input.txt") as file:
    list = [int(line) for line in file.readlines()]

print(sum(list[index] > list[index - 3] for index in range(3, len(list))))
