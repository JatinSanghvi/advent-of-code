def enhance(image, enhancement):
    enhanced_image = [["0"] * (len(image[0]) - 2) for _ in range(len(image) - 2)]
    for ri in range(1, len(image) - 1):
        for ci in range(1, len(image[0]) - 1):
            index = "".join(image[ri2][ci2] for ri2 in range(ri - 1, ri + 2) for ci2 in range(ci - 1, ci + 2))
            enhanced_image[ri - 1][ci - 1] = enhancement[int(index, 2)]
    return enhanced_image


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    enhancement = ["1" if pix == "#" else "0" for pix in lines[0].rstrip()]
    image = [["1" if pix == "#" else "0" for pix in line.rstrip()] for line in lines[2:]]
    times = 50

    # Apply border.
    image = [["0"] * len(image[0]) for _ in range(times * 2)] + image + [["0"] * len(image[0]) for _ in range(times * 2)]
    image = [["0"] * (times * 2) + row + ["0"] * (times * 2) for row in image]

    for _ in range(times):
        image = enhance(image, enhancement)

    print(sum(len([pix for pix in row if pix == "1"]) for row in image))


solve("input-test.txt")
solve("input.txt")
