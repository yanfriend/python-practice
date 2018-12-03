class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = set([x for i, x in enumerate(fronts) if backs[i] == x])
        mfront = min([x for x in fronts if x not in same] or [float('inf')])
        mback = min([x for x in backs if x not in same] or [float('inf')])
        return min(mfront, mback) if mfront!=float('inf') or mback!=float('inf') else 0

print Solution().flipgame([1],[1])
