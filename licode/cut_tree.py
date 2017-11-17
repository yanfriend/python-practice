import collections


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest: return -1
        m = len(forest);
        n = len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()

        sx = 0;
        sy = 0
        ret = 0
        for i in range(len(trees)):
            tx, ty = trees[i][1], trees[i][2]
            step = self.bfs(forest, sx, sy, tx, ty)
            if step == -1: return -1
            ret += step
            sx, sy = tx, ty
        return ret

    def bfs(self, forest, sx, sy, tx, ty):
        visited = set()
        visited.add((sx, sy))
        qu = collections.deque()
        qu.append((sx, sy))
        step = 0
        sential = (None, None)
        qu.append(sential)
        while len(qu) > 1:
            x, y = qu.popleft()
            if x is None: step += 1; qu.append(sential); continue
            if x == tx and y == ty: return step
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = x + di;
                ny = y + dj
                if 0 <= nx < len(forest) and 0 <= ny < len(forest[0]) and (nx, ny) not in visited and forest[nx][
                    ny] != 0:
                    qu.append((nx, ny))
                    visited.add((nx, ny))
        return -1

print Solution().cutOffTree(
    [
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
)
