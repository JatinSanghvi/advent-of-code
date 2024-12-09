from typing import List


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        line = file.readline().rstrip("\n")

    # Create disk image.
    disk: List[int | None] = []

    file_id = 0
    is_file = True
    for char in line:
        length = int(char)
        for _ in range(length):
            disk.append(file_id if is_file else None)
        file_id += 1 if is_file else 0
        is_file = not is_file

    # Defragment disk.
    left, right = 0, len(disk) - 1
    while True:
        while left < right and disk[left] is not None:
            left += 1
        while left < right and disk[right] is None:
            right -= 1
        if left < right:
            disk[left], disk[right] = disk[right], disk[left]
            left += 1
            right -= 1
        else:
            break

    # Calculate filesystem checksum.
    checksum = 0
    for pos, id_ in enumerate(disk):
        checksum += (id_ or 0) * pos

    print(checksum)


solve("input-test.txt")  # 1928
solve("input.txt")  # 6359213660505
