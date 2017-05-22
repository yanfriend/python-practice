class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=''
        for i in range(0,len(s)):
            tmp=self.check(s, i,i)
            if len(tmp)>len(ret):
                ret=tmp
            tmp=self.check(s, i, i+1)
            if len(tmp)>len(ret):
                ret=tmp
        return ret

    def check(self,s,i,j):
        if j>=len(s):
            return ''
        ret=''
        while i>=0 and j<len(s) and s[i]==s[j]:
            ret=s[i:j+1]
            i-=1
            j+=1
        return ret
