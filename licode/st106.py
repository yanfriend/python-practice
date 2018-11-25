"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None

        #try:
        ind=inorder.index(postorder.pop())
        #except:
        #    return None
        
        node=TreeNode(inorder[ind])
        node.left=self.buildTree(inorder[:ind],postorder)
        node.right=self.buildTree(inorder[ind+1:],postorder)
        return node
