import collections
import operator

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        id = 2;
        sizes = collections.defaultdict(int)
        m = len(grid);
        n = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n): return 0
            if grid[i][j] == 0 or grid[i][j] > 1: return 0
            grid[i][j]=id
            cnt = 1  # meet 1
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                cnt += dfs(x, y)
            return cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[id] = dfs(i, j)
                    id += 1
        if not sizes: return 1
        ans = max(sizes.iteritems(), key=operator.itemgetter(1))[1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen=set()
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= x < m and 0 <= y < n:
                            seen.add(grid[x][y])
                    ans = max(ans, 1+sum([sizes[s] for s in seen]))
        return ans

# print Solution().largestIsland([[1,0],[0,1]])  # 3
# print Solution().largestIsland([[1]])
print Solution().largestIsland([[1,1],[1,0]])
