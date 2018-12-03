import collections


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        ans = [None for i in range(len(quiet))]

        def dfs(root):
            if ans[root] is not None: return ans[root]
            ans[root] = root
            for nei in graph[root]:
                cand = dfs(nei)
                if quiet[cand] < quiet[ans[root]]: ans[root] = cand
            return ans[root]

        return map(dfs, range(len(quiet)))

print Solution().loudAndRich([[0,2],[1,2]], [0,1,2])
