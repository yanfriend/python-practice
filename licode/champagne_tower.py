class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [0] * (100 + 1)
        dp[0] = poured
        for r in range(query_row):
            dp_next =[0] * (100 + 1)
            for c in range(r + 1):
                dp[c] -= 1
                if dp[c] > 0:
                    dp_next[c] += dp[c] / 2.0
                    dp_next[c + 1] += dp[c] / 2.0
                # else: dp[c]=0
            print dp_next
            dp=dp_next
        return min(1.0, dp[query_glass])

# print Solution().champagneTower(1,1,0) # 0
print Solution().champagneTower(4,2,1)
