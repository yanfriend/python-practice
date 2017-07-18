"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "a aacecaaa".

Given "abcd", return "dcb abcd".
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i]+s




    # time out below
    #     pal_end=len(s)-1
    #     for i in range(len(s)-1,-1,-1):
    #         if self.is_pan(s,i):
    #             pal_end=i
    #             break
    #     return s[len(s)-1:pal_end:-1]+s
    #
    # def is_pan(selfs,s,end):
    #     l=0; r=end
    #     while (l<=end):
    #         if s[l]!=s[r]: return False
    #         l+=1; r-=1
    #     return True

print Solution().shortestPalindrome("aacecaaa")
