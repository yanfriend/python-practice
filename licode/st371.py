class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        part_sum=a^b
        carry=(a&b)<<1
        while carry!=0:
            import ipdb; ipdb.set_trace()

            tmp=part_sum
            part_sum^=carry
            carry&=tmp
            carry=carry<<1
        return part_sum

print Solution().getSum(-1,1)
