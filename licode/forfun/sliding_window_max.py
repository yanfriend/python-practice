import collections


def maxSlidingWindow(nums, k):
    ret=[]
    qu=collections.deque()

    for i in range(len(nums)):
        while len(qu)>0 and qu[0]<=i-k:
            qu.popleft()
        while len(qu)>0 and nums[qu[-1]]<nums[i]:
            qu.pop()
        qu.append(i)

        if i>=k-1: ret.append(nums[qu[0]])
    return ret

print maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
