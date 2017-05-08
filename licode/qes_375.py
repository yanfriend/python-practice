class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[float('inf') for i in range(0,n+1)] for i in range(0,n+1)]

        # formular: dp(i,k-1)+k+dp(k+1,j), so must increase from j, descrease from i
        for j in range(1, n+1):
            for i in reversed(range(1,j)): # range(start, stop(exclude), step)
                # import ipdb; ipdb.set_trace()
                for k in range(i+1,j):
                    dp[i][j]=min(self.cal(dp,i,j),k+max(self.cal(dp,i,k-1),self.cal(dp,k+1,j)))
                    self.pp(dp,n)

        return self.cal(dp,1,n)

    def cal(self,dp,i,j):
        if i>=j: return 0
        if i==j-1: return i
        return dp[i][j]

    def pp(self,dp,n):
        for i in range(1,n+1):
            for j in range(1,n+1):
                print '{} '.format(dp[i][j]),
            print '\n'
        # import ipdb; ipdb.set_trace()

print Solution().getMoneyAmount(7)
