def binary_search(arr, val):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        gues = arr[mid]
        if gues == val:
            return mid
        elif gues < val:
            low = mid + 1
        elif gues > val:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    print(binary_search(arr=[1,3,5,7,9], val=4))