def solve(stream):
    for index in range(3, len(stream)):
        if stream[index] != stream[index - 1] and \
                stream[index] != stream[index - 2] and \
                stream[index] != stream[index - 3] and \
                stream[index - 1] != stream[index - 2] and \
                stream[index - 1] != stream[index - 3] and \
                stream[index - 2] != stream[index - 3]:
            print(index + 1)
            return


def main():
    solve('mjqjpqmgbljsphdztnvjfqwrcgsmlb')  # 7
    solve('bvwbjplbgvbhsrlpgdmjqwftvncz')  # 5
    solve('nppdvjthqldpwncqszvftbrmjlhg')  # 6
    solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')  # 10
    solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')  # 11

    with open('input.txt') as file:
        solve(file.readline())  # 1658


if __name__ == '__main__':
    main()
