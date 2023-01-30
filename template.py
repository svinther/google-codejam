import sys


def runtestcase(tc):
    pass


def runtestcases():
    T = int(input())
    for tc in range(T):
        runtestcase(tc + 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            sys.stdin = fin
            runtestcases()
    else:
        runtestcases()
