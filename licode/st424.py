import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret=0
        begin=end=0
        max_rep=0

        map=collections.defaultdict(int)

        while end<len(s):
            map[s[end]]+=1
            max_rep=max(max_rep, map[s[end]])

            while end-begin+1-max_rep>k:
                map[s[begin]]-=1
                for i in range(27):
                    max_rep=max(max_rep,map[chr(i+ord('A'))])
                begin+=1
            ret=max(ret, end-begin+1)
            end+=1

        return ret
