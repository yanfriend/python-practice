class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0]=True

        for i in range(1,len(p)+1):
            import ipdb;ipdb.set_trace()

            for j in range(1,len(s)+1):
                if p[i-1]==s[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif p[i-1]=='.':dp[i][j]=dp[i-1][j-1]
                elif p[i-1]=='*':dp[i][j]=dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]

        return dp[len(p)][len(s)]

print Solution().isMatch('','*')
