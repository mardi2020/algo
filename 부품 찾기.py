n = int(input())
data = list(map(int, input().split()))
k = int(input())
require = list(map(int, input().split()))
data.sort()

def bs(target, start, end):
    if start > end :
        return False
    mid = (start + end) // 2

    if data[mid] == target:
        return True
    elif data[mid] < target :
        return bs(target, mid+1, end)
    else:
        return bs(target, start, mid-1)


for target in require:
    if not bs(target, 0, n-1) :
        print("no" ,end=' ')
    else :
        print("yes", end=' ')
    