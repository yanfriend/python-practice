class Solution(object):
    class TreeNode(object):
        def __init__(self, val):
            self.left=self.right=None
            self.val=val
            self.sum=0
            self.dup=1

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ret=[0]*len(nums)
        root=None
        for i in range(len(nums)-1,-1,-1):
            root=self.insert_node(root, nums, i, 0, ret)
        return ret

    def insert_node(self,root,nums,ind, pre_sum, ret):
        if not root:
            node=Solution.TreeNode(nums[ind])
            ret[ind]=pre_sum
            return node
        elif nums[ind]<root.val:
            root.left=self.insert_node(root.left,nums,ind,pre_sum,ret)
            root.sum+=1
            return root
        elif nums[ind]>root.val:
            root.right=self.insert_node(root.right,nums,ind,pre_sum+root.sum+root.dup,ret)
            return root
        else:
            root.dup+=1
            ret[ind]=root.sum+pre_sum
            return root
