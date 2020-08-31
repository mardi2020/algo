cach = [0] * 100

cach[1] = cach[2]  = 1
n = 99

for i in range(3, n+1):
    cach[i] = cach[i-1] + cach[i-2]

print(cach[n])