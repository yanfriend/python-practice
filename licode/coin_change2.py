import copy


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0]*(amount+1);dp[0]=1
        for j in range(1,amount+1):

            import ipdb;ipdb.set_trace()

            new_dp=[0]*(amount+1);new_dp[0]=1

            for i in range(len(coins)):
                if j-coins[i]>=0:
                    new_dp[j]+=dp[j-coins[i]]
            dp=new_dp
        return dp[amount]

print Solution().change(5,[1,2,5])
