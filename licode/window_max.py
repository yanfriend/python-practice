# def window_max(arr,k):
#     ret=float('-inf')
#     begin_ind=0
#     curr_sum=0
#     for i,val in enumerate(arr):
#         curr_sum += val
#         if i-begin_ind+1>k:
#             curr_sum-=arr[begin_ind]
#             begin_ind+=1
#         if i-begin_ind+1==k:
#             ret=max(ret,curr_sum)
#     return ret
#
# print window_max([2,5,6,7,2,8,5,4,3,9,4],2) # 13

def window_max_sum(arr,k):
    assert(len(arr)>=3*k)

    dp_left=[float('-inf')]*len(arr)
    dp_right=[float('-inf')]*len(arr)
    dp_mid=[float('-inf')]*len(arr)

    ret=float('-inf')
    begin_ind=0
    curr_sum=0

    for i,val in enumerate(arr):
        curr_sum += val
        if i-begin_ind+1>k:
            curr_sum-=arr[begin_ind]
            begin_ind+=1
        if i-begin_ind+1==k:
            ret=max(ret,curr_sum)
            dp_left[i]=ret
            dp_mid[i]=curr_sum

    curr_sum=0
    end_index=len(arr)-1
    ret=float('-inf')
    for i in range(len(arr)-1,-1,-1):
        curr_sum+=arr[i]
        if end_index-i+1>k:
            curr_sum-=arr[end_index]
            end_index-=1
        if end_index-i+1==k:
            ret=max(ret,curr_sum)
            dp_right[i]=ret

    print dp_left
    print dp_mid
    print dp_right

    ret=float('-inf')
    begin_ind=k
    curr_sum=0
    for i in range(k,len(arr)-k):
        curr_sum+=arr[i]
        if i-begin_ind+1>k:
            curr_sum-=arr[begin_ind]
            begin_ind+=1
        if i-begin_ind+1==k:
            ret=max(ret,curr_sum+dp_left[begin_ind-1]+dp_right[i+1])
    return ret

print window_max_sum([2,5,6,7,2,8,5,4,3,9,4],2) # 39

