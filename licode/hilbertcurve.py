# -*- coding: utf-8 -*-

class Solution(object):
    def hilbert_curve(self, x, y, iter):
        if iter == 0: return 1

        harfLen = 2**(iter-1) # 1 << (iter - 1)  # 1(iter==1),2,4,8,16, length of each limit
        harfNum = 2**(2*(iter-1)) # 1 << (2 * (iter - 1))  # 1(iter==1), 4, 16, 64  numbers in each limit

        if x >= harfLen and y >= harfLen:  # top, right.
            return 2 * harfNum + self.hilbert_curve(x - harfLen, y - harfLen, iter - 1)
        elif x < harfLen and y >= harfLen:  # top, left.
            return harfNum + self.hilbert_curve(x, y - harfLen, iter - 1)
        elif x < harfLen and y < harfLen:  # bottom, left
            return self.hilbert_curve(y, x, iter - 1)
        else:  # bottom, right.  x>=harfLen and y<harfLen
            # 设原来坐标(a,b) => (-b, -a) => (2*borderLen - 1 - b, borderLen - 1 - a) = (x, y)
            #     // => a = borderLen - 1 - y, b = 2*borderLen - 1 - x
            # see pic how points are counted
            return 3 * harfNum + self.hilbert_curve(harfLen - 1 - y, 2 * harfLen - 1 - x, iter - 1)


# 问你在iter这张图中在(x, y)坐标的点是第几个, ok
print Solution().hilbert_curve(0, 0, 1)  # 1
print Solution().hilbert_curve(0, 1, 1)  # 2
print Solution().hilbert_curve(1, 1, 1)  # 3
print Solution().hilbert_curve(1, 0, 1)  # 4

print Solution().hilbert_curve(1, 1, 2)  # 3
print Solution().hilbert_curve(2, 2, 2)  # 9

print Solution().hilbert_curve(1, 1, 2)  # 3, 9, 7, 13
print Solution().hilbert_curve(2, 2, 2)
print Solution().hilbert_curve(1, 3, 2)
print Solution().hilbert_curve(3, 1, 2)
