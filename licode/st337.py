# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cache={}
        return self.cache_rob(root,cache)

    def cache_rob(self,root, cache):
        if not root:return 0
        if cache.get(root,-1) != -1:
            return cache[root]

        exclude=self.cache_rob(root.left,cache)+self.cache_rob(root.right,cache)

        inc=root.val
        if root.left:
            inc+=self.cache_rob(root.left.left,cache) + self.cache_rob(root.left.right,cache)
        if root.right:
            inc+=self.cache_rob(root.right.left,cache) + self.cache_rob(root.right.right,cache)

        ret= max(inc, exclude)
        cache[root]=ret
        return ret
