import collections


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = collections.defaultdict(int)

        def find(x):
            if x in uf:
                if x != uf[x]:
                    uf[x] = uf[find(uf[x])]
            else:
                uf[x] = x
            return uf[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                uf[px] = uf[py]  # ??

        for i, j in stones:
            union(i, ~j)
        return len(stones) - len({find(x) for x in uf})

print Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])

