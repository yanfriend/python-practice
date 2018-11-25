# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum_leaves(root, True)

    def sum_leaves(self, root, left_leave):
        if root is None: return 0

        if root.left==root.right==None:
            return root.val if left_leave else 0
        return self.sum_leaves(root.left, True) + self.sum_leaves(root.right, False)
