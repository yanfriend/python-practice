class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        qu = []
        row = len(grid);
        col = len(grid[0])

        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    qu.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        cnt = 0
        while len(qu) > 0:
            cnt += 1
            newq = []
            for i, j in qu:
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                        grid[i + di][j + dj] = 2
                        newq.append((i + di, j + dj))
                        fresh -= 1
            qu = newq

        return max(0, cnt - 1) if fresh == 0 else -1

