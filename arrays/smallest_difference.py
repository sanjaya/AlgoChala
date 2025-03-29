def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pair=[]
    indexX , indexY = 0 , 0
    diff = float('inf')
    while indexX < len(arrayOne) and indexY < len(arrayTwo):
        if abs(arrayOne[indexX]-arrayTwo[indexY]) < diff:
            diff = abs(arrayOne[indexX]-arrayTwo[indexY])
            pair=[arrayOne[indexX],arrayTwo[indexY]]
        if(arrayOne[indexX] < arrayTwo[indexY]):
            indexX+=1
        else:
            indexY+=1
    return pair

print(smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))