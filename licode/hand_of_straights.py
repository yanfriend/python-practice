import collections


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        counter=collections.Counter(hand)
        while counter:
            k=sorted(counter)[0]
            for i in range(k,k+W):
                if counter[i]==0: return False
                counter[i]-=1
                if counter[i]==0: del counter[i]
        return True

print Solution().isNStraightHand([1,2,3,4,5], 4)
