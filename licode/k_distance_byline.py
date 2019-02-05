
def k_distance(inp, target, k):

    def edit_distance(w, t):
        dp=[[0]*(len(t)+1) for i in range(len(w)+1)]
        for i in range(1, len(dp)):
            dp[i][0]=i
        for j in range(1, len(dp[0])):
            dp[0][j]=j

        for i in range(1,len(w)+1):
            for j in range(1,len(t)+1):
                if t[j-1]==w[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[len(dp)-1][len(dp[0])-1]

    ret=[]
    for w in inp:
        dist=edit_distance(w,target)
        if dist<=k:
            ret.append(w)
    return ret

# print k_distance(["abcd", "abc", "abd", "ad", "c", "cc"], 'abcd', 2) # ['abcd', 'abc', 'abd', 'ad']
print k_distance(["ad", "c", "cc"], 'abcd', 2)
