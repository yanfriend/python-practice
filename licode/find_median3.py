def find_median(numbers):
    def helper(k):
        l = 0
        r = (1 << 32) - 1

        while l < r:
            mid = (l + r) / 2
            cnt = 0; ret = 0  # error 3,  this should be inside the loop
            for n in numbers:
                if n <= mid:
                    cnt += 1
                    ret = max(ret, n)
            if cnt == k + 1:
                return ret
            elif cnt < k + 1:
                l = mid + 1
            else:
                r = mid
        return l  # error 1, used ret

    if len(numbers) % 2 == 1:  # error 2, should use mod
        return helper(len(numbers) / 2)
    else:
        return (helper(len(numbers) / 2 - 1) + helper(len(numbers) / 2)) / 2.0


numbers=[1,2,2,2,2,4,5] # 2
print find_median(numbers)

numbers=[1,2,2,2,2,4] # 2
print find_median(numbers)


print find_median([3,2,5,3,1]) # 1,2,3,3,5   # get 3
print find_median([1,1,1,3,1]) #  should be 1.  # 1,1,1,1,3

print find_median([3,2,5,3,1,6,7,8,10]) # 1,2,3,3,5,6,7,8  # get 5

print find_median([3,2,5,3,1,6,7,8]) # 1,2,3,3,5,6,7,8  # get 4.0
print find_median([3,2,3,3,1,6,7,8]) # 1,2,3,3,3,6,7,8  # get 3
