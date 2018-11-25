class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0: return 0

        sign=(dividend>0 and divisor<0) or (divisor>0) and (dividend<0)
        dividend=abs(dividend)
        divisor=abs(divisor)

        moves=0
        while dividend>=(divisor<<1):
            divisor <<= 1
            moves +=1

        quo=0
        while moves>=0:
            quo <<= 1
            if dividend>=divisor:
                dividend -= divisor
                quo += 1
            divisor >>= 1
            moves -= 1
        return -quo if sign else quo


print Solution().divide(-1,1)
