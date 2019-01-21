

class Solution(object):

    def findN(self,n,numbers):
        l=0; r=1<<32-1
        while l<r:
            mid=(l+r)/2

            count=0; res=0
            for num in numbers:
                if num<=mid:
                    count+=1
                    res=max(res,num)

            if count==n+1: return res
            elif count>n+1: r=mid
            else: l=mid+1
        return l

    def find_median(self, numbers):
        n=len(numbers)
        if n%2==1: # odd numbers
            return self.findN(n/2, numbers)
        else:
            return (self.findN(n/2-1, numbers) + self.findN(n/2, numbers))/2.0


print Solution().find_median([3,2,5,3,1]) # 1,2,3,3,5   # get 3
print Solution().find_median([3,2,5,3,1,6,7,8]) # 1,2,3,3,5,6,7,8  # get 4
#
print Solution().find_median([1,1,1,3,1]) #  should be 1.  # 1,1,1,1,3

