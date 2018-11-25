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
            for j in range(0,len(s)+1): # note: this from 0 for match nothing
                if j>0 and (s[j-1]==p[i-1] or p[i-1]=='.'):
                    dp[i][j]=dp[i-1][j-1]
                elif p[i-1]=='*':
                    dp[i][j]=dp[i-2][j] \
                        or (j>=1 and (p[i-2]==s[j-1] or p[i-2]=='.') and dp[i][j-1]) # s previous letter
                        #  front line x* match 0;
                        # the second line matches 1 or more, so s trace back!

        return dp[len(p)][len(s)]

print Solution().isMatch('aa','a*')
