import sys
from collections import defaultdict, deque


def bfs(E, s):
    dists = {}
    D = deque([(s, 0)])
    SEEN = {s}
    while D:
        n, d = D.popleft()
        dists[n] = d
        for nb in E[n]:
            if nb in SEEN:
                continue
            SEEN.add(nb)
            D.append((nb, d + 1))
    return dists


def dot(E, Q, A):
    print("graph {")
    print("  ", Q, f'[label="{Q} (Q)"]')
    print("  ", A, f'[label="{A} (A)"]')
    for j in E.keys():
        for c in E[j]:
            print(
                "  ",
                j,
                "--",
                c,
            )
    print("}")


def runtestcase(tc):
    J, C, A, Q = map(int, input().split())
    E = defaultdict(list)
    for _ in range(C):
        U, V = map(int, input().split())
        E[U].append(V)
        E[V].append(U)

    # dot(E, Q, A)

    # dists to all j's from Q and A
    dq, da = bfs(E, Q), bfs(E, A)
    # Q's graph and A's graph (nodes one can get to before the other can)
    gq, ga = set(), set()
    for j in range(1, J + 1):
        if j in dq:
            if j not in da or dq[j] < da[j]:
                gq.add(j)
        if j in da:
            if j not in dq or da[j] < dq[j]:
                ga.add(j)

    # Q can not get to A's graph ?
    if not ga & dq.keys():
        return "SAFE"

    # cycles in A's graph, corridors >= junctions ?
    jcount = len(ga)
    ccount = sum(len(c) for j, c in E.items() if j in ga) // 2
    if ccount >= jcount:
        return "SAFE"

    return max(d for j, d in dq.items() if j in ga) * 2


def runtestcases():
    T = int(input())
    for t in range(T):
        result = runtestcase(t + 1)
        print(f"Case #{t+1}:", result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            sys.stdin = fin
            runtestcases()
    else:
        runtestcases()
