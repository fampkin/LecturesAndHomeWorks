def f_max(arr: list) -> int:
    if len(arr) == 0:
        return 0
    fm = f_max(arr[1:])
    return arr[0] if arr[0] > fm else fm

print(f_max([1]))