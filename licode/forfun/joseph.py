def joseph1(nums,k):
    # nums from 1 to N
    if not nums: return -1

    ind=0
    while len(nums)>1:
        ind=(ind+k-1)%len(nums)
        nums.pop(ind)

    return nums[0]

print joseph1([1,2,3,4,5,6,7,8,9,10],3) # 4

print joseph1([1],3) # 4
print joseph1([1,2],3) # 4
print joseph1([1,2,3],3) # 4

print '************'

def joseph2(nums,k):
    # nums from 1 to N
    if not nums: return -1

    ret=0
    for i in range(2,len(nums)+1):
        ret=(ret+k)%i

    return nums[ret]

print joseph2([1,2,3,4,5,6,7,8,9,10],3) # 4
