class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        MAGIC = 100000  # len(R)<18, square root<9; half <100000. that how magic comes
        cnt = 0
        L = int(L);
        R = int(R)

        def is_palin(stri):
            strx = str(stri)
            return strx == strx[::-1]

        for x in range(1, MAGIC):
            strx = str(x)
            newp = strx + strx[::-1]
            if L <= int(newp) ** 2 <= R and is_palin(int(newp) ** 2): cnt += 1
            newp = strx + strx[::-1][1:]
            if L <= int(newp) ** 2 <= R and is_palin(int(newp) ** 2): cnt += 1

        return cnt


print Solution().superpalindromesInRange('1','2')
