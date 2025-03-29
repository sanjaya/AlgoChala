class validateSubSequence:

    @staticmethod
    def isValidSubsequence(array, sequence):
        if (len(sequence) > len(array)):
            return False
        arrayIdx = 0
        seqIdx = 0
        while arrayIdx < len(array) and seqIdx < len(sequence):
            if array[arrayIdx] == sequence[seqIdx]:
                seqIdx += 1
            arrayIdx += 1
        return seqIdx == len(sequence)

    @staticmethod
    def isValidSubsequencefor(array, sequence):
        if (len(sequence) > len(array)):
            return False
        seqIdx = 0
        for value in array:
            if seqIdx == len(sequence) :
                break
            if value == sequence[seqIdx]:
                seqIdx += 1
        return seqIdx == len(sequence)
'''
Both are O(n) and O(1) solution.
For me for is default thought.
'''

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 19]
output = validateSubSequence.isValidSubsequence(array, sequence)
print(output)

