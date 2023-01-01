import sys


def runtestcase():
    N = int(input())
    D = list(map(int, input().split()))
    assert len(D) == N
    l, r = 0, len(D) - 1
    result = 0
    seen = -1
    while l <= r:
        if D[l] < D[r]:
            if D[l] >= seen:
                result += 1
                seen = D[l]
            l += 1
        else:
            if D[r] >= seen:
                result += 1
                seen = D[r]
            r -= 1
    return result


def runtestcases():
    numtc = int(input())
    for t in range(numtc):
        result = runtestcase()
        print(f"Case #{t+1}:", result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            sys.stdin = fin
            runtestcases()
    else:
        runtestcases()
