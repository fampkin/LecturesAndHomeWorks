def count_els(arr: list) -> int:
    if len(arr) == 0:
        return 0
    return 1 + count_els(arr[1:])

print(count_els([]))