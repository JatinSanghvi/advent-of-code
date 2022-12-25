def solve(path):
    with open(path) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    def decimal_value(snafu: str) -> int:
        decimal = 0
        for snafu_digit in snafu:
            if snafu_digit == '=': value = -2
            elif snafu_digit == '-': value = -1
            elif snafu_digit == '0': value = 0
            elif snafu_digit == '1': value = 1
            elif snafu_digit == '2': value = 2

            decimal = (decimal * 5) + value

        return decimal

    sum = 0
    for line in lines:
        sum += decimal_value(line)

    def snafu_value(decimal: int) -> str:
        snafu = ''
        while decimal != 0:
            value = (((decimal % 5) + 2) % 5) - 2
            if value == -2: snafu = '=' + snafu
            elif value == -1: snafu = '-' + snafu
            elif value == 0: snafu = '0' + snafu
            elif value == 1: snafu = '1' + snafu
            elif value == 2: snafu = '2' + snafu

            decimal = (decimal - value) // 5

        return snafu

    print(snafu_value(sum))


def main():
    solve('input-test.txt')  # 2=-1=0
    solve('input.txt')  # 20-=0=02=-21=00-02=2


if __name__ == '__main__':
    main()
