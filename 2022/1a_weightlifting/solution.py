import sys
from collections import deque
from functools import reduce, lru_cache
from io import StringIO
from itertools import permutations
from operator import add
from pathlib import Path


def get_cost(fromstate, tostate):
    f, t = fromstate, tostate
    if f == t:
        return 0

    for i in range(len(f)):
        if i == len(t):
            return len(f) - len(t)
        if f[i] != t[i]:
            return len(f) - i + get_cost(f[:i], t)

    assert len(t) > len(f)
    return len(t) - len(f)


def solve(input_):
    numtc = int(input_.readline())
    for tc in range(numtc):
        E, W = [int(x) for x in input_.readline().split()]

        startstate = endstate = tuple()
        S = []
        for e in range(E):
            nweights = reduce(
                add,
                [
                    list(chr(ord("a") + i)) * int(x)
                    for i, x in enumerate(input_.readline().split())
                ],
            )
            wcombos = set(permutations(nweights))
            S.append(wcombos)
        S.append({endstate})

        @lru_cache(maxsize=None)
        def findmin(e, s):
            if e == len(S):
                return 0

            return min(get_cost(s, sn) + findmin(e + 1, sn) for sn in S[e])

        print(f"Case #{tc + 1}:", findmin(0, startstate))


def test1():
    print()
    input_ = Path("tc1.txt").read_text()
    solve(StringIO(input_))


if __name__ == "__main__":
    solve(sys.stdin)
