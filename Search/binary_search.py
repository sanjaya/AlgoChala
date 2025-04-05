def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end :
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1

print(binary_search([1, 2, 3, 4, 5], 5)) # Output: 2