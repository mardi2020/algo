n = int(input())
# 2 * n 크기의 직사각형

cach = [0] * 1000
cach[0] = 1
cach[1] = 3

for i in range(2, n):
    cach[i] = (cach[i-1] + 2 * cach[i-2]) % 796796

print(cach[n-1])