import collections


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        taken = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]:
                taken[b].append(A.pop())
        return [taken[b].pop() if b in taken else A.pop() for b in B]


print Solution().advantageCount([2,0,4,1,2], [1,3,0,0,2])
