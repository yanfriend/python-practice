def min_cities(prices, budget):
    budget=int(budget*100)
    prices=[int(p*100) for p in prices]

    dp=[float('inf')]*(budget+1)
    dp[0]=0

    for i in range(len(prices)):
        for j in range(len(dp)):
            if j-prices[i]>=0 and dp[j-prices[i]]<float('inf'):
                dp[j]=min(dp[j], dp[j-prices[i]]+1)

    return dp[-1]

print min_cities([10.01,20.02,15.01], 30.03)
