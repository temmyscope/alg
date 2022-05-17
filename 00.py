def insertionSort(data: list):
    length: int = len(data)

    for i in range(1, length):
        currentValue = data[i]

        j = i-1
        while j >= 0 and currentValue < data[j]:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = currentValue
        
    return data


print(
    #[12, 2, 5, 13, 9, 7, 4, 1, 10, 15]
    insertionSort([1, 4, 17, 3, 90, 79, 4, 6, 81])
)