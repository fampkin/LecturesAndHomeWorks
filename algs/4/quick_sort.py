import random
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        l = []
        m = []
        r = []
        
        for n in arr:
            if n < pivot:
                l.append(n)
            elif n > pivot:
                r.append(n)
            else:
                m.append(n)
                
        return quick_sort(l) + m + quick_sort(r)
    
print(quick_sort([1,3,2,4]))