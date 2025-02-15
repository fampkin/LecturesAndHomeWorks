def summa(arr: list) -> int:
    if len(arr) == 0:
        return 0
    return arr[0] + summa(arr[1:])

print(summa([1,2,3,4,5]))