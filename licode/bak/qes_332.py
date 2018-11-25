import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ret_len=len(tickets)+1

        from_to=collections.defaultdict(list)
        for pair in tickets:
            from_to[pair[0]].append(pair[1])
            from_to[pair[0]].sort()

        ret=['JFK']

        visited={} # tuple -> true

        self.dfs(ret, from_to, visited, len(tickets), 'JFK')
        return ret

    def dfs(self, ret, from_to, visited, length, root):
        if len(visited)==length:
            return True

        to_list=from_to[root]
        for to_node in to_list:
            if visited.get((root,to_node),False):
                continue
            visited[(root,to_node)]=True
            ret.append(to_node)
            if self.dfs(ret, from_to, visited, length, to_node):
                return True
            del(visited[(root,to_node)])
            ret.pop()
        return False

print Solution().findItinerary([['JFK','a'],['a','b'],['b','JFK'], ['JFK','d']])
