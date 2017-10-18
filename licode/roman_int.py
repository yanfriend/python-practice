class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_to_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ret=letter_to_num[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if letter_to_num[s[i]]<letter_to_num[s[i+1]]:
                ret-=letter_to_num[s[i]]
            else:
                ret+=letter_to_num[s[i]]
        return ret

print Solution().romanToInt('DCXXI')






'''
13. Roman to Integer
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question.
'''
