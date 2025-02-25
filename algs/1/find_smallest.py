def findSmallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest_ind = i
            smallest = arr[i]
    return smallest_ind

