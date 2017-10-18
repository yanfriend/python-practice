
def max_distance(arr):
    min_val=float('inf')
    max_val=float('-inf')
    ret=0

    for alist in arr:
        max_val=max(max_val,alist[-1])
        min_val=min(min_val,alist[0])
        ret=max(ret,max_val-min_val)

    return ret

print max_distance([[1,2,3],[4,5], [1,2,3]])
