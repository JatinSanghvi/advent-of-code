import hashlib


def solve(path):
    with open(path) as file:
        key = file.readline()

    for suffix in range(1, 2000000):
        hash = hashlib.md5((key + str(suffix)).encode('utf-8'))
        if hash.hexdigest().startswith('00000'):
            print(suffix)
            return


def main():
    solve('input-test1.txt')  # 609043
    solve('input-test2.txt')  # 1048970
    solve('input.txt')  # 282749


if __name__ == '__main__':
    main()
