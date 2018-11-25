def maxsum_at_least_k_size(arr, k):
    # max sum till i
    pre_sum=0
    max_sum=[0]*len(arr)
    for i,num in enumerate(arr):
        max_sum[i]=max(pre_sum+num,num)
        pre_sum=max_sum[i]

    # max sum size of k
    sum_k=0
    for i in range(k):
        sum_k+=arr[i]
    ret=sum_k
    for i in range(k,len(arr)):
        sum_k=sum_k+arr[i]-arr[i-k]
        ret=max(ret,sum_k,sum_k+max_sum[i-k])
    return ret

print maxsum_at_least_k_size([1,1,1,1,1,1],2) # 6
print maxsum_at_least_k_size([-4, -2, 1, -3],2) # -1
