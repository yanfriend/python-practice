import collections


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # idea: freq for nums freq, append_freq, for how many subseq can add next ending at the num.
        counter=collections.Counter(nums)
        append_freq=collections.defaultdict(int)
        for num in nums:
            if counter[num]==0: continue
            if append_freq[num]>0:
                append_freq[num]-=1
                append_freq[num+1]+=1
            elif counter[num+1]>0 and counter[num+2]>0:
                counter[num+1]-=1
                counter[num+2]-=1

                import ipdb; ipdb.set_trace()

                append_freq[num+2]=append_freq[num+2]+1
            else:
                return False
            counter[num]-=1
        return True

print Solution().isPossible([1,2,3,3,4,5])


