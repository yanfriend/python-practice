def coinChange(coins, amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0

    for i in range(1,len(dp)):
        for coin in coins:
            if i<coin: continue
            if dp[i-coin]!=float('inf'):
                dp[i]=min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1


    # dp=[[0]*(amount+1) for _ in range(len(coins)+1)]
    #
    # for i in range(1,len(coins)+1):
    #     for j in range(1,amount+1):
    #         if j>=coins[i-1]:
    #             dp[i][j]= min(dp[i][j],dp[i-1][j-coins[i-1]]+1)
    #         else:
    #             dp[i][j]=dp[i-1][j]
    #
    # return dp[len(coins)][amount] if dp[len(coins)][amount]!=0 else -1

print coinChange([1,2,5],11)

print coinChange([2],3)
