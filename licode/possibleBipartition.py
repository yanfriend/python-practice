import collections


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for d1, d2 in dislikes:
            graph[d1].append(d2)
            graph[d2].append(d1)

        color = {}

        def dfs(root, c=0):
            if not root: return True
            if root in color:
                if color[root] != c: return False
                else: return True
            color[root] = c
            for nei in graph[root]:
                if not dfs(nei, c ^ 1): return False
            return True

        for i in range(1, N + 1):
            if i in color: continue
            if not dfs(i, 0): return False
        return True


print Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]])
