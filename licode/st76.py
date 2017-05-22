import collections

"""
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter=collections.Counter(t)

        l=r=0
        cnt=len(t)
        start_ind=l
        min_len=float('inf')

        while r<len(s):
            ch=s[r]
            if counter[ch]>0:
                cnt-=1
            counter[ch]-=1

            while cnt==0:
                if min_len>r-l+1:
                    start_ind=l
                    min_len=r-l+1
                if counter[s[l]]>=0:
                    cnt+=1
                counter[s[l]]+=1
                l+=1

            r+=1

        return '' if min_len==float('inf') else s[start_ind:start_ind+min_len]

print Solution().minWindow('ab','b')
