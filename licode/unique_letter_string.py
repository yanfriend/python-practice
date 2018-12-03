class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type S: str
        :rtype: int
        """
        d = {}
        res = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [-1]
            else:
                k, j = d[c][-2:]
                res += (j - k) * (i - j)
            d[c].append(i)

        for c in d:
            k, j = d[c][-2:]
            res += (j - k) * (len(s) - j)

        return res


print Solution().uniqueLetterString("ABA")
# print Solution().uniqueLetterString("ABC")