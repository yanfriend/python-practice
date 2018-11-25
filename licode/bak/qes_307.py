class NumArray(object):
    class SegmentTreeNode(object):
        def __init__(self,start,end):
            self.start=start
            self.end=end
            self.left=None
            self.right=None
            self.sum=0

    def build_tree(self,nums,ld,rd):
        if ld>rd: return None
        if ld==rd:
            stn=NumArray.SegmentTreeNode(ld,rd)
            stn.sum=nums[ld]
            return stn
        else:
            mid=(ld+rd)/2
            stn=NumArray.SegmentTreeNode(ld,rd)
            stn.left=self.build_tree(nums,ld,mid)
            stn.right=self.build_tree(nums,mid+1,rd)
            stn.sum=stn.left.sum+stn.right.sum
            return stn


    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root=self.build_tree(nums,0,len(nums)-1)



    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.rec_update(self.root,i,val)

    def rec_update(self,root,i,val):
        if root.start==root.end==i:
            diff=val-root.sum
            root.sum=val
            return diff
        if i<=(root.start+root.end)/2:
            diff=self.rec_update(root.left,i,val)
        else:
            diff=self.rec_update(root.right,i,val)
        root.sum+=diff
        return diff

    def sumRange(self,i,j):
        return self.srh(self.root,i,j)

    def srh(self, root, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if root.start==i and root.end==j: return root.sum
        mid=(root.start+root.end)/2
        if j<=mid:
            return self.srh(root.left, i,j)
        elif i>mid:
            return self.srh(root.right,i,j)
        else:
            return self.srh(root.left, i, mid)+self.srh(root.right, mid+1,j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

nums=[9, -8]
obj = NumArray(nums)
print obj.update(0,3)

import ipdb; ipdb.set_trace()

print obj.sumRange(1,1)
