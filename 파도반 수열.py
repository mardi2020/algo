import sys
input = sys.stdin.readline

T = int(input())

data = [0] * 101
data[0] = 1
data[1] = 1
data[2] = 1

for i in range(3, 101):
    data[i] = data[i-2]+data[i-3]

for _ in range(T):
    N = int(input())
    print(data[N-1])