def solve(stream):
    for index in range(13, len(stream)):
        if len(set(stream[index - 13: index + 1])) == 14:
            print(index + 1)
            return


def main():
    solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb')  # 19
    solve('bvwbjplbgvbhsrlpgdmjqwftvncz')  # 23
    solve('nppdvjthqldpwncqszvftbrmjlhg')  # 23
    solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')  # 29
    solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')  # 26

    with open('input.txt') as file:
        solve(file.readline())  # 2260


if __name__ == '__main__':
    main()
