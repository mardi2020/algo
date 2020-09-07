n = int(input())

arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda grade: grade[1])

for i in range(n):
    print(arr[i][0], end=' ')