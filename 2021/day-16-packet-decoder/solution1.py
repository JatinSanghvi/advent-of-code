def version_sum(binary):
    ver_sum = int(binary[0:3], 2)
    typeid = int(binary[3:6], 2)

    if typeid == 4:
        for index in range(6, len(binary), 5):
            if binary[index] == "0": break
        index += 5

    elif binary[6] == "0":
        length = int(binary[7:22], 2)
        end_index = 22 + length
        index = 22
        while index < end_index:
            (sub_ver_sum, sub_index) = version_sum(binary[index:])
            ver_sum += sub_ver_sum
            index += sub_index
    else:
        packets = int(binary[7:18], 2)
        index = 18
        for _ in range(packets):
            (sub_ver_sum, sub_index) = version_sum(binary[index:])
            ver_sum += sub_ver_sum
            index += sub_index

    # print("version_sum({0}) => ({1}, {2})".format(binary, ver_sum, index))
    return (ver_sum, index)


def solve(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file.readlines()]

    for line in lines:
        binary = "".join(["{0:04b}".format(int(char, 16)) for char in line])
        print(version_sum(binary)[0])


solve("input-test-1.txt")
solve("input.txt")
