import sys
from io import StringIO

def nextchange(line, i):
    c = line[i]
    for cn in line[i+1:]:
        if cn != c:
            return cn


lines = [l.strip() for l in sys.stdin.readlines() if l.strip()]
testcases = int(lines[0])
for tc, tcinp in enumerate(lines[1:]):
    result = StringIO()
    result.write(f"Case #{tc + 1}: ")
    for i, c in enumerate(tcinp):
        if i < len(tcinp) - 1:
            next = nextchange(tcinp, i)
            if next and c < next:
                result.write(c * 2)
                continue
        result.write(c)
    print(result.getvalue())
