class TwoNumberSum:
    @staticmethod
    def twoNumberSum(array, targetSum):
        array.sort()
        left = 0
        right = len(array) - 1
        while left < right:
            currentSum = array[left] + array[right]
            if currentSum == targetSum:
                return [array[left], array[right]]
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
        return []

# Call the method directly since it's static
output = TwoNumberSum.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(output)
# Time O(nlon(n)) | sapce O(1) - More stable compare to hash based solution as it takes O(n) sapce.
