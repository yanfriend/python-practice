import collections

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        import ipdb;ipdb.set_trace()

        if s1==s2: return True
        if collections.Counter(s1)!=collections.Counter(s2):
            return False

        for i in range(1,len(s1)):
            # if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
            if self.isScramble(s1[:i],s2[-i:]) \
                    and self.isScramble(s1[-i:], s2[:i]): return True

        return False

print Solution().isScramble('abc','bca')
