import collections

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # for O(n) running time, limit unique letters 1-> 26, find the longest string with at least k repeating letters.
        ret=0
        # for i in range(1,27):
        #     ret=max(ret,self.longestUnique(s,k,i))

        ret=max(ret,self.longestUnique(s,k,1))
        return ret

    def longestUnique(self,s,k,uniqueTarget):
        import ipdb; ipdb.set_trace()

        map=collections.defaultdict(int)
        begin=end=0
        unique_letter=0
        no_smaller_than_k=0
        ret=0

        while end<len(s):
            if map[s[end]]==0: unique_letter+=1
            map[s[end]] += 1
            if map[s[end]]==k: no_smaller_than_k+=1
            end+=1

            if map[s[begin-1]]==k:
                no_smaller_than_k-=1
            if map[s[begin]]>uniqueTarget:
                map[s[begin]]-=1
                begin+=1

            if unique_letter==uniqueTarget and unique_letter==no_smaller_than_k:
                ret=max(ret, end-begin)
        return ret

print Solution().longestSubstring('aaabb', 3)
