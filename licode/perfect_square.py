def numSquares(num):
    dp=[float('inf')]*(num+1)
    dp[0]=0

    for i in range(1,num+1):
        for j in range(1,int(i**0.5)+1):
            dp[i]=min(dp[i], dp[i-j*j]+1)
    return dp[-1]

print numSquares(12)
print numSquares(13)


