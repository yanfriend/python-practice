class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        ret=0

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    ret+=1
        return ret

print Solution().countSubstrings('abc') # 3
print Solution().countSubstrings('aaa') # 6
