import hashlib


def solve(path):
    with open(path) as file:
        key = file.readline()

    for suffix in range(1, 20000000):
        hash = hashlib.md5((key + str(suffix)).encode('utf-8'))
        if hash.hexdigest().startswith('000000'):
            print(suffix)
            return


def main():
    solve('input.txt')  # 9962624


if __name__ == '__main__':
    main()
