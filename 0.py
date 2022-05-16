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

        
def isPrime(number: int) -> bool:
    #all even numbers above 2 can't be prime
    if number > 3 and number % 2 == 0:
        return False
    # 0, 1, 2 and 3 are Prime
    if number in [0, 1, 2, 3]:
        return True

    for i in range(3, number):
        if i != number and number % i == 0:
            return False
    return True

print(
    insertionSort([12, 2, 5, 13, 9, 7, 4, 1, 10, 15])
)