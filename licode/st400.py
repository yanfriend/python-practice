# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        length=1
        cnt=9

        while(n>length*cnt):
            n-=length*cnt
            start*=10
            length+=1
            cnt*=10

        import ipdb; ipdb.set_trace()

        start += (n-1)/length
        return str(start)[(n-1)%length]

print Solution().findNthDigit(12)

# print Solution().findNthDigit(11)
