class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        import collections
        ad=collections.defaultdict(set)
        for abc in allowed:
            ad[abc[0:2]].add(abc[2]) # use either a tuple, or string

        def dfs(bottom, upper):
            if len(bottom)==2 and len(upper)==1: return True
            if len(bottom)-len(upper)==1: return dfs(upper, '')
            ind=len(upper)
            next_set=ad[bottom[ind:ind+2]]
            for ch in next_set:
                if dfs(bottom,upper+ch): return True
            return False

        if len(bottom)==1: return True
        return dfs(bottom,'')

