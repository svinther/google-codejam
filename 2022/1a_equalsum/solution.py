import sys

# import subprocess
# p = subprocess.Popen([r"C:\Users\svso\AppData\Local\Programs\Python\Python39\python.exe", "local_testing_tool.py"], text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# stdout = p.stdin
# stdin = p.stdout

stdin = sys.stdin
stdout = sys.stdout

numtc = stdin.readline()
numtc = int(numtc)
for _ in range(numtc):
    numints = stdin.readline()
    numints = int(numints)
    assert numints != -1

    pow2 = []
    while True:
        b = 2 ** len(pow2)
        if b <= 10**9:
            pow2.append(b)
        else:
            break

    myints = list(range(1025, 1025 + (numints - len(pow2))))

    stdout.write(" ".join([str(i) for i in myints + pow2]))
    stdout.write("\n")
    stdout.flush()
    otherints = stdin.readline()
    otherints = [int(s) for s in otherints.strip().split()]

    sumleft, sumright = 0, 0
    left, right = [], []
    for i in myints + otherints + list(reversed(pow2)):
        if sumleft < sumright:
            left.append(i)
            sumleft += i
        else:
            right.append(i)
            sumright += i

    assert sumright == sumleft

    stdout.write(" ".join([str(i) for i in left]))
    stdout.write("\n")
    stdout.flush()
