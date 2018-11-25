import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=collections.Counter(s)
        visited={}
        ret='0'

        for ch in s:
            if visited.get(ch,False): continue

            # import ipdb; ipdb.set_trace()

            while ret[-1]>ch and c[ret[-1]]>0:
                visited[ret[-1]]=False
                ret=ret[:-1]
            ret+=ch
            c[ch]-=1
            visited[ch]=True
        return ret[1:]

print Solution().removeDuplicateLetters('bcabc')

