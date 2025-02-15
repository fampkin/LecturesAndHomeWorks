def binary_sear(arr: list, low:int, mid:int, high:int, c) -> int:
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return mid if arr[0] == c else None 
    elif arr[mid] == c:
        return mid
    elif arr[mid] < c:
        return binary_sear(arr=arr, low=mid+1, mid=(low+high)//2, high=high-1, c=c)
    elif arr[mid] > c:
        return binary_sear(arr=arr, low=low, mid=(low+high)//2, high=(low+high)//2-1, c=c)
    
    
l=[]
print(binary_sear(arr=l, low=0, mid=(0+len(l))//2, high=len(l)-1, c=1))
