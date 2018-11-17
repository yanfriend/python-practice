class Solution(object):
    def containVirus(self, grid):
        row = len(grid); col = len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < row and 0 <= nc < col:
                    yield nr, nc  # good to learn

        def dfs(r, c):  # r,c must have value 1 for recursive call
            if (r, c) not in visited:
                visited.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))  # frontier has no dup; while perimeter can have.
                        perimeter[-1] += 1

        ans = 0
        while True:
            visited = set()
            regions = []
            frontiers = []
            perimeter = []

            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        regions.append(set())
                        frontiers.append(set())
                        perimeter.append(0)
                        dfs(i, j)

            if not regions: break
            max_frontiers = max(frontiers, key=len)  # max affected
            frontier_ind = frontiers.index(max_frontiers)

            ans += perimeter[frontier_ind]  # not len(max_frontiers) for duplication.

            for i in range(len(regions)):
                if i == frontier_ind:
                    for r, c in regions[frontier_ind]:
                        grid[r][c] = -1
                else:
                    for r, c in regions[i]: # affecting
                        for nr, nc in neighbors(r, c):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1

        return ans


print Solution().containVirus([
    [1,1,1,0,0,0,0,0,0],
    [1,0,1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0,0,0]])
