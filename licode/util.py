# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Driver program to test above function
"""
Constructed binary tree is
            20
          /   \
        10     30
      /  \
     5    15
"""
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)


def pre_print(root):
    if not root: return
    print root.val,
    pre_print(root.left)
    pre_print(root.right)
