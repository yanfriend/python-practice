"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len=len(nums1)+len(nums2)
        if total_len%2==0:
            return (self.findm(total_len/2, nums1, nums2, 0, 0)+self.findm(total_len/2+1, nums1, nums2, 0,0)) /2.0
        else:
            return self.findm(total_len/2+1, nums1, nums2, 0, 0)

    def findm(self, k, nums1, nums2, s1,s2): # k begins with 1, kth element
        import ipdb; ipdb.set_trace()

        if s1>=len(nums1): return nums2[s2+k-1] # return kth from nums2
        if s2>=len(nums2): return nums1[s1+k-1]
        if k==1: return min(nums1[s1], nums2[s2])

        m1=s1+k/2-1
        m2=s2+k/2-1
        mid1= nums1[m1] if m1<len(nums1) else float('inf')
        mid2= nums2[m2] if m2<len(nums2) else float('inf')
        if mid1>mid2:
            return self.findm(k-k/2,nums1,nums2,s1,s2+k/2)
        else:
            return self.findm(k-k/2,nums1,nums2,s1+k/2,s2)

print Solution().findMedianSortedArrays([1,2],[3,4])



