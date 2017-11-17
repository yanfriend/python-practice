import bisect


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        active=[]
        for day,pos in enumerate(flowers):
            i=bisect.bisect(active,pos)
            neighbors=active[i-(i!=0):i+1]
            for nei in neighbors:
                if abs(nei-pos)-1==k:
                    return day+1
            active.insert(i,pos)
        return -1

print Solution().kEmptySlots([1,3,2],1)

