import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b):
    r = b % a
    if r == 0 :
        return a
    else :
        return gcd(r, a)

for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    data = data[1:]
    ssum = 0
    for i in range(n):
        for j in range(i+1, n):
            ssum += gcd(data[i], data[j])
    print(ssum)




