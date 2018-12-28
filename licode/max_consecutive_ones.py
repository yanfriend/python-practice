def max_consecutive_ones(numbers):

    ans=0; current=0; last=0
    for i in range(len(numbers)):
        current+=1
        if numbers[i]==0:
            last=current
            current=0
        ans=max(ans,current+last)
    return ans


print max_consecutive_ones([1,0,1,1,0])  # Output: 4


