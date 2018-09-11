class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import collections
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        for i in range(1, N + 1):
            dist[i] = float('inf')

        qu = collections.deque()
        qu.append((K, 0))

        # import ipdb; ipdb.set_trace()

        while (len(qu) > 0):
            node, the_dist = qu.popleft()
            if the_dist < dist[node]:
                qu.append((node, the_dist))
                dist[node] = the_dist
                for nei, nei_dist in graph[node]:
                    qu.append((nei, the_dist + nei_dist))
        return max(dist.values()) if max(dist.values()) < float('inf') else -1

print Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
