class TwoNumberSum:
    @staticmethod
    def twoNumberSum(array, targetSum):
        complements = {}
        for num in array:
            complement = targetSum - num
            if complement in complements:
                return [num,complement]
            else:
                complements[num] = "Available"
        return[]


# Call the method directly since it's static
output = TwoNumberSum.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 16)
print(output)
#O(n) time and  O(n) space. Not considered to be stable.
