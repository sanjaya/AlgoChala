class SortedSquaredArray:
    @staticmethod
    def sortedSquaredArray(array):
        sqArray = [0] * len(array)
        start = 0
        end = len(array) - 1
        # sqArray = [0 for _ in array]
        for i in range(len(array) - 1, -1, -1):
            if abs(array[start]) > abs(array[end]):
                sqArray[i] = array[start] * array[start]
                start += 1
            else:
                sqArray[i] = array[end] * array[end]
                end -= 1
        return sqArray

# O(n) time and  O(n) space. Thought. Execution
input = [1, 2, 3, 5, 6, 8, 9]
output = SortedSquaredArray.sortedSquaredArray(input)
print(output)