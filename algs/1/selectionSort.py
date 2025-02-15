from find_smallest import findSmallest

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr


print(selectionSort([1,10,2,3,42,32]))
        