

def move_zeros(arr):
    fr=fl=0
    while fr<len(arr):
        if arr[fr]==0:
            fr+=1
            continue
        arr[fr],arr[fl]=arr[fl],arr[fr]
        fr+=1
        fl+=1

arr=[1,0,3,4,0,0,9,8]
move_zeros(arr)
print arr
