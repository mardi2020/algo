n, k = map(int, input().split())

coin = list()

for _ in range(n):
    x = int(input())
    coin.append(x)

coin.sort(reverse=True)

res = 0
for c in coin:
    res += k // c
    k %= c

print(res)