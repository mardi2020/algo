def binarySearch1(arr, target, start, end):
    if start > end : 
        return
    
    mid = (start + end) // 2

    if arr[mid] == target :
        return mid
    elif arr[mid] < target :
        return binarySearch1(arr, target, mid+1, end)
    else:
        return binarySearch1(arr, target, start, mid-1)
    
def binarySearch2(arr, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            start = mid + 1
        else :
            end = mid - 1