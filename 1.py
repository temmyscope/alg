def binarySearch( arr: list[int], item: int):
    length = len(arr)
    startIndex: int = 0
    stopIndex: int = length-1

    while( startIndex <= stopIndex ):
        middleIndex: int = startIndex+(stopIndex-startIndex)//2

        if( arr[middleIndex] == item ):
            return middleIndex
        elif( arr[middleIndex] < item ):
            startIndex=middleIndex+1
        else:
            stopIndex=middleIndex-1
        
    return -1

def searchForItem(itemsList: list, item) -> int:
    length = len( itemsList )
    startIndex = 0
    stopIndex = length

    while True:
        middleIndex = (startIndex + stopIndex)//2
        if itemsList[middleIndex] == item:
            return middleIndex
        elif itemsList[middleIndex] > item:
            stopIndex = middleIndex
        elif itemsList[middleIndex] < item:
            startIndex = middleIndex

print(
    #searchForItem( [1, 3, 4, 5, 7, 9, 10, 12, 13, 17, 21], 17)
    binarySearch([-5, -2, -1, 0, 1, 2, 4], 4)
    #[2, 5, 13, 9, 7, 4, 1, 10, 15]
)