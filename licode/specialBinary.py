class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = i = 0
        res = []
        for j, v in enumerate(S):
            count = count + 1 if v == '1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1 : j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])

# print Solution().makeLargestSpecial('10110010')
print Solution().makeLargestSpecial('101110110000')
# ()(( ()(()) ))