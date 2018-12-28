

class Solution(object):

    def findN(self,n,numbers):
        l=0; r=1<<32-1
        while l<r:
            mid=(l+r)/2
            count=len([num for num in numbers if num<mid])
            if count>=n: r=mid
            else: l=mid+1
        return l

    def find_median(self, numbers):
        n=len(numbers)
        if n%2==1: # odd numbers
            return self.findN(n/2, numbers)
        else:
            return (self.findN(n/2-1, numbers) + self.findN(n/2, numbers))/2.0


print Solution().find_median([3,2,5,3,1])

print Solution().find_median([3,2,5,3,1,6,7,8]) # 1,2,3,3,5,6,7,8

