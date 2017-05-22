import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1=collections.Counter(s1)
        c2=collections.Counter(s2[:len(s1)])

        end=len(s1)-1

        while end<len(s2)-1:
            if c1==c2: return True
            end+=1
            c2[s2[end]]+=1
            c2[s2[end-len(s1)]]-=1
            if c2[s2[end-len(s1)]]<=0:
                del c2[s2[end-len(s1)]]
        return c1==c2

print Solution().checkInclusion('ab','eidbaooo')
