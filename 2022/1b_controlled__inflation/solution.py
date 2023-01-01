import sys
from functools import lru_cache


def runtestcase():
    N, P = map(int, input().split())
    np = [list(map(int, input().split())) for _ in range(N)]

    @lru_cache(maxsize=None)
    def recurse(n, pas):
        psorted = list(sorted(np[n]))
        cost = sum(abs(psorted[i] - psorted[i + 1]) for i in range(len(psorted) - 1))
        cost_mi, cost_ma = abs(pas - psorted[0]), abs(pas - psorted[-1])
        if n == len(np) - 1:
            return min(cost + cost_mi, cost + cost_ma)

        return min(
            cost + cost_mi + recurse(n + 1, psorted[-1]),
            cost + cost_ma + recurse(n + 1, psorted[0]),
        )

    return recurse(0, 0)

def runtestcases():
    T = int(input())
    for t in range(T):
        result = runtestcase()
        print(f"Case #{t + 1}:", result)


if __name__ == "__main__":
    sys.setrecursionlimit(10**4)
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            sys.stdin = fin
            runtestcases()
    else:
        runtestcases()
