
def shortest_comb(target, items):
    dp=[float('inf')]*(target+1)
    dp[0]=0

    for i in range(1, len(items)+1):
        for j in range(1, target+1):
            if j>=items[i-1] and dp[j-items[i-1]] != float('inf'):
                    dp[j] = min(dp[j - items[i-1]] + 1, dp[j])

    return dp[-1]

# print shortest_comb(9, [1,2,4,5]) # 2
print shortest_comb(8, [1, 3, 5, 6]) # 2
