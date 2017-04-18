class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)/2+1):
            if len(s)%i != 0:
                continue
            str = s[0:i]
            import ipdb; ipdb.set_trace()
            for j in range(1,len(s)/i+1):
                print s[j*i:j*i+i]
                if str==s[j*i:j*i+i]:
                    continue
                break
            if j==len(s)/i:
                return True
        return False



print Solution().repeatedSubstringPattern('abab')
