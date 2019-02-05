
def descending3(numbers):
    n=len(numbers)
    dp=[float('-inf')]*n

    for i in range(1, n):
        cnt=0
        for j in range(i):
            if numbers[j]>numbers[i]:
                cnt+=1
        if cnt!=0:
            dp[i]=cnt

    new_dp=[0]*n
    for i in range(1,n):
        for j in range(i):
            if numbers[j] > numbers[i] and dp[j]!=float('-inf'):
                new_dp[i]+=dp[j]
    return sum(new_dp)

print descending3([10,12,8,5,4,9])
