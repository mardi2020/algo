import sys
input = sys.stdin.readline

n = list(input().rstrip())
n = sorted(n, reverse=True)

ssum = 0
for e in n:
    ssum += int(e)

if n[-1] != '0' or ssum % 3 != 0:
    print(-1)
    sys.exit(0)

print("".join(n))
