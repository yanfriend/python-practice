class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret=[0]
        self.helper(root,None,ret)
        return max(0,ret[0]-1)

    def helper(self,root,pval,ret):
        if not root: return

        lv=self.helper(root.left,root.val,ret)
        rv=self.helper(root.riht,root.val,ret)
        ret[0]=max(ret[0],lv+rv+1)

        if root.val==pval:
            return max(lv,rv)+1
        else:
            return 0
