# copied
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        evenPal = lambda sp : int(sp + sp[::-1])
        oddPal = lambda sp : int(sp + sp[::-1][1:])
        sn, n = n, int(n)
        if len(sn) == 1: return str(n - 1) # ensure have difference. diff is 1
        ans = -999999999999999999
        mid = len(sn) / 2
        for sp in sn[:mid], sn[:mid + 1], str(int(sn[:mid]) * 10):
            p = int(sp)
            for pal in evenPal, oddPal:
                for d in -1, 0, 1:
                    val = pal(str(p + d))
                    if val == n: continue
                    ans = min(ans, val, key = lambda x : (abs(x - n), x))
        return str(ans)

print Solution().nearestPalindromic('123')
print Solution().nearestPalindromic('8')

