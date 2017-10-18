
def move_zeros(arr):
    p=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[p],arr[i]=arr[i],arr[p]
            p+=1

arr=[1,0,3,4,0,0,9,8]
move_zeros(arr)
print arr
