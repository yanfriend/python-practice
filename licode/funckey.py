# sort by surfix array
def sort2(l1,l2):
    while l1<len(nums) and l2<len(nums) and nums[l1]==nums[l2]:
        l1+=1; l2+=1
    if l1==len(nums) or nums[l1]<nums[l2]: return -1
    if l2==len(nums) or nums[l1]>nums[l2]: return 1
    else: return 0

nums = [10, 20, 30, 20, 25]
# result: 0,3,1,4,2
idx=range(len(nums))
idx.sort(cmp=sort2)
print idx

nums = [10,20,30,25]
# expect 10,20,25,30, i.e. 0,1,3,2
idx=range(len(nums))
idx.sort(cmp=sort2) # correct
print idx
