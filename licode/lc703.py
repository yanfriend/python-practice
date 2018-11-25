"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream.
For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length >= k-1 and k >= 1.

"""

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        for i in range(0, len(nums) - k):  # while len(nums) > k: easier to understand
            heapq.heappop(nums)
        self.nums = nums
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k > len(self.nums):
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
k=3
nums = [4,5,8,2]
obj = KthLargest(k, nums)

print obj.add(3)
print obj.add(5)
print obj.add(10)
print obj.add(9)
print obj.add(4)
