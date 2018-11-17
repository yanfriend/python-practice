import collections

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        s = set([i for i, v in enumerate(routes) if S in v])
        t = set([i for i, v in enumerate(routes) if T in v])
        graph = collections.defaultdict(set)
        for i in xrange(len(routes)):
            for j in xrange(i + 1, len(routes)):
                if set(routes[i]).intersection(set(routes[j])):
                    graph[i].add(j);
                    graph[j].add(i)

        if s.intersection(t): return 0
        visited = set()
        q = [(start, 1) for start in s]
        while len(q) > 0:
            newq = []
            for st, step in q:
                if st in t: return step
                if st in visited: continue
                visited.add(st)
                for nei in graph[st]:
                    if nei in visited: continue
                    newq.append((nei, step + 1))
            q = newq
        return -1

print Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12)
