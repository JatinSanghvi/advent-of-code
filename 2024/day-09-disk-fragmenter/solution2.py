from typing import List, Tuple


def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        line = file.readline().rstrip("\n")

    # Create disk image.
    files: List[Tuple[int, int, int]] = []
    spaces: List[Tuple[int, int]] = []

    file_id = 0
    disk_pos = 0
    is_file = True
    for char in line:
        length = int(char)
        if is_file:
            files.append((file_id, disk_pos, length))
            file_id += 1
        else:
            spaces.append((disk_pos, length))

        disk_pos += length
        is_file = not is_file

    # Defragment disk.
    files = files[::-1]
    for fi, (f_id, f_start, f_len) in enumerate(files):
        for si, (s_start, s_len) in enumerate(spaces):
            if s_start >= f_start:
                break
            if s_len >= f_len:
                spaces[si] = (s_start + f_len, s_len - f_len)
                files[fi] = (f_id, s_start, f_len)
                break

    # Calculate filesystem checksum.
    checksum = 0
    for f_id, f_start, f_len in files:
        for f_pos in range(f_start, f_start + f_len):
            checksum += f_id * f_pos

    print(checksum)


solve("input-test.txt")  # 2858
solve("input.txt")  # 6381624803796
