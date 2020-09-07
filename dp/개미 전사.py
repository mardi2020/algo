n = int(input())
data = list(map(int, input().split()))

cach = [0] * 100
cach[0] = data[0]
cach[1] = max(data[0], data[1])
for i in range(2, len(data)):
    cach[i] = max(cach[i-1], cach[i-2]+data[i])


print(cach[n-1])
