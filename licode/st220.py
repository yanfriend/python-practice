class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t<0 or k<=0: return False
        w=t+1
        my_dict={}

        for i,n in enumerate(nums):
            if i>k:
                del my_dict[nums[i-k-1]/w]
            key=n/w
            if key in my_dict:
                return True
            if key-1 in my_dict and abs(my_dict[key-1]-n)<=t: # only one such key; otherwise have returned True
                return True
            if key+1 in my_dict and abs(my_dict[key+1]-n)<=t:
                return True
            my_dict[key]=n
        return False

print Solution().containsNearbyAlmostDuplicate([1,3,1],1,1)
