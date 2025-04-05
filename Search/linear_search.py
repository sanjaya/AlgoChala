def linear_search(arr, target):
    index = -1
    for i in range(len(arr)) :
        if arr[i]== target:
            return i
    return index

print(linear_search([3, 7, 2, 5], 5))