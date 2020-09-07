n = int(input())

data = [[0]*n]*n

for i in range(n):
    data[i] = list(map(int, input().split()))

d = [0] * 1000
for i in range(n):
    d[0] = min(data[i][0])
d[1] = 