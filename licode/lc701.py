"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        head = TreeNode(float('-inf'))
        head.right = root

        self.helper(head, root, val)
        return head.right

    def helper(self, parent, curr, val):
        if curr is None:
            new_node = TreeNode(val)
            self.assign(parent, new_node)
        elif curr.val < val:
            self.helper(curr, curr.right, val)
        else:
            self.helper(curr, curr.left, val)

    def assign(self, parent, newNode):
        if parent.val < newNode.val:
            parent.right = newNode
        else:
            parent.left = newNode


'''
# much better than mine.

public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root==null) return new TreeNode(val);
        if(val<root.val) root.left=insertIntoBST(root.left, val);
        else root.right=insertIntoBST(root.right, val);
        return root;
    }
'''
