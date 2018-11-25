class TreeNode(object):
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

class Solution(object):
    def __init__(self):
        self.cnt=0

    def countUnivalSubtrees(self, root):
        """
        :rtype: int
        """
        self.helper(root)
        return self.cnt

    def helper(self, root):
        if not root: return True, None

        lb, lv=self.helper(root.left)
        rb, rv=self.helper(root.right)

        if lb and rb:
            lv=lv or root.val
            rv=rv or root.val
            if lv==rv==root.val:
                self.cnt+=1
                return True, root.val
        return False, 0

root=TreeNode(5)
root.left=TreeNode(4)
root.left.left=TreeNode(4)
root.left.right=TreeNode(4)
root.right=TreeNode(5)
root.right.right=TreeNode(5)

print Solution().countUnivalSubtrees(root)


