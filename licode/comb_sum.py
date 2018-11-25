def comb_sum(nums,target):
    ret=[]
    dfs(nums,target,ret,[],0)
    return ret

def dfs(nums,target,ret,path,ind):
    if target==0: ret.append(path)
    if target<0 or ind==len(nums): return

    for i in range(ind,len(nums)):
        dfs(nums,target-nums[i],ret,path+[nums[i]],i)

print comb_sum([2, 3, 6, 7],7)
