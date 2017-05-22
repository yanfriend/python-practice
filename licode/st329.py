class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0

        dp=[[float('-inf')]*len(matrix[0]) for _ in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix,i,j,dp)

        return max([max(row) for row in dp])

    def dfs(self, matrix,i,j,dp):
        if dp[i][j]>float('-inf'): return dp[i][j]

        dp[i][j]=1

        delta=[(1,0),(-1,0),(0,1),(0,-1)]
        for di,dj in delta:
            if matrix[i][j] > self.get_val(matrix,i+di, j+dj):
                dp[i][j]=max(dp[i][j], self.dfs(matrix,i+di, j+dj ,dp)+1)
        return dp[i][j]

    def get_val(self, matrix, i, j):
        if i<0 or j<0: return float('inf')
        if i>=len(matrix) or j>=len(matrix[0]): return float('inf')
        return matrix[i][j]

print Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
