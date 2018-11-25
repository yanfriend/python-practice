import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        from_to=collections.defaultdict(list)
        for pair in tickets:
            from_to[pair[0]].append(pair[1])
            from_to[pair[0]].sort(reverse=True)

        def dfs(root):
            to_list=from_to[root]
            while to_list:
                to_node=to_list.pop()
                dfs(to_node)
            ret.appendleft(root)

        ret=collections.deque()
        dfs('JFK')
        return list(ret)
