#bubble sort algorithm

def bubbleSort( arr: list ):
    length = len(arr)
    for i in range(length-1):  
        for j in range(length-1):  
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 

def optimizedBubbleSort( arr: list ):
    hasSwapped = True
    length = len(arr)
    total_iteration = 0

    while hasSwapped :
        hasSwapped = False
        for j in range(length - total_iteration - 1):  
            if( arr[j] > arr[j+1] ):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                hasSwapped = True
        total_iteration += 1  
    return arr

#insertion sort algorithm
def insertionSort(arr: list):
    length = len(arr)
    for i in range(1, length):
        tempValue = arr[i]

        j = i - 1
        while ( j >= 0 ) and (tempValue < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = tempValue
    return arr

        


print(
    insertionSort([12, 2, 5, 13, 9, 7, 4, 1, 10, 15])
)