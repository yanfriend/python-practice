def isMatched(s,p):
    rows=len(p)
    cols=len(s)

    # assert
    dp=[[False]*(cols+1) for _ in range(rows+1)]
    dp[0][0]=True

    # special case for '', with *
    for i in range(1,rows+1):
        if p[i-1]=='*':
            dp[i][0]=dp[i-1][0]

    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if s[j-1]==p[i-1] or p[i-1]=='?':
                dp[i][j]=dp[i-1][j-1]
            elif p[i-1]=='*':
                dp[i][j]=dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
    return dp[rows][cols]

print isMatched('','*')
print isMatched('aaaab','a*')
print isMatched('aaaab','ab*')
