def find_median(numbers):

    def findk(k):
        l=0; r=1<<32-1

        while l<r:
            mid = (l+r)/2
            cnt=0
            closest=float('-inf')
            for n in numbers:
                if n<=mid:
                    cnt+=1
                    closest=max(closest,n)
            if cnt==k+1:
                return closest
            elif cnt>k+1:
                r=mid
            else:
                l=mid+1
        return l

    if len(numbers)%2==1:
        return findk(len(numbers)/2)
    else:
        # return (findk(len(numbers)/2-1)+findk(len(numbers)/2))/2.0
        half_max = findk(len(numbers) / 2 - 1)
        cnt=0
        closest=float('inf')
        for n in numbers:
            if n > half_max:
                cnt += 1
                closest = min(closest, n)
        if cnt==len(numbers)/2:
            return (half_max+closest)/2.0
        else:
            return half_max


print find_median([3,2,5,3,1]) # 1,2,3,3,5   # get 3
print find_median([1,1,1,3,1]) #  should be 1.  # 1,1,1,1,3
print find_median([3,2,5,3,1,6,7,8,10]) # 1,2,3,3,5,6,7,8  # get 5

print find_median([3,2,5,3,1,6,7,8]) # 1,2,3,3,5,6,7,8  # get 4.0
print find_median([3,2,3,3,1,6,7,8]) # 1,2,3,3,3,6,7,8  # get 3
