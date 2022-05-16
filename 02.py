"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""
def medianOfTwoLists(listOne: list[int], listTwo: list[int]) -> float|int:
    tempList = [ *listOne, *listTwo ]
    tempList.sort()
    length = len(tempList)
    midPoint = length%2
    if length%2 == 0:
        return (
            tempList[(length//2)] + tempList[(length//2) - 1]
        )/2
    else:
        return tempList[length//2]

print(
    medianOfTwoLists([1, 2], [3, 4])
    #medianOfTwoLists([1, 3, 5, 6], [2, 4, 7, 9])
)