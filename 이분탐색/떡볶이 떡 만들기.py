n, m = map(int, input().split())

ttok = list(map(int, input().split()))

start, end = 0, max(ttok)

height = 0
while start <= end :
    mid = (start + end) // 2
    
    tot = 0
    for e in ttok:
        if e > mid : 
            tot += (e - mid)
    
    if tot < m :
        end = mid - 1
    
    else :
        start = mid + 1
        height = mid

print(height)