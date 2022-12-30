import sys
from functools import reduce
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


def findmin(S, s):
    if not S:
        return 0

    return min(get_cost(s, sn) + findmin(S[1:], sn) for sn in S[0])


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

        print(f"Case #{tc + 1}:", findmin(S, startstate))


def test1():
    print()
    input_ = Path("tc1.txt").read_text()
    solve(StringIO(input_))


if __name__ == "__main__":
    solve(sys.stdin)
