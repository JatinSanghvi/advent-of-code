def solve(path):
    with open(path) as file:
        lines = file.readlines()

    dimensions = [[int(dim) for dim in line.split('x')] for line in lines]
    face_areas = [[dims[0] * dims[1], dims[1] * dims[2], dims[2] * dims[0]] for dims in dimensions]
    paper_areas = [2 * (areas[0] + areas[1] + areas[2]) + min(areas) for areas in face_areas]
    print(sum(paper_areas))


def main():
    solve('input-test.txt')  # 101
    solve('input.txt')  # 1606483


if __name__ == '__main__':
    main()
