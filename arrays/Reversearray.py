# Reversing array .
def reverseArray(lst):
    start = 0
    end = len(lst)-1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst


print(reverseArray([1, 2, 3, 4, 5]))