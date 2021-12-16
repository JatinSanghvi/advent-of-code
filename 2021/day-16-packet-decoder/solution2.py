from functools import reduce


def version_sum(binary):
    type_id = int(binary[3:6], 2)

    if type_id == 4:
        bin_value = ""
        for index in range(6, len(binary), 5):
            bin_value += binary[index + 1:index + 5]
            if binary[index] == "0": break

        value = int(bin_value, 2)
        index += 5
    else:
        sub_values = []

        if binary[6] == "0":
            length = int(binary[7:22], 2)
            end_index = 22 + length
            index = 22
            while index < end_index:
                (sub_value, sub_index) = version_sum(binary[index:])
                sub_values.append(sub_value)
                index += sub_index
        else:
            packets = int(binary[7:18], 2)
            index = 18
            for _ in range(packets):
                (sub_value, sub_index) = version_sum(binary[index:])
                sub_values.append(sub_value)
                index += sub_index

        if type_id == 0: value = sum(sub_values)
        elif type_id == 1: value = reduce(lambda x, y: x * y, sub_values)
        elif type_id == 2: value = min(sub_values)
        elif type_id == 3: value = max(sub_values)
        elif type_id == 5: value = 1 if sub_values[0] > sub_values[1] else 0
        elif type_id == 6: value = 1 if sub_values[0] < sub_values[1] else 0
        elif type_id == 7: value = 1 if sub_values[0] == sub_values[1] else 0

    # print("version_sum({0}) => ({1}, {2})".format(binary, value, index))
    return (value, index)


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    for line in lines:
        binary = "".join(["{0:04b}".format(int(char, 16)) for char in line])
        print(version_sum(binary)[0])


solve("input-test-2.txt")
solve("input.txt")
