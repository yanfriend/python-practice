# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret=[]
        st=[]
        if not root: return ret
        st.append(root)

        prev=None
        while st:

            import ipdb;ipdb.set_trace()

            ele=st[-1]
            if (ele.right is None and ele.left==prev) or (ele.right and ele.right==prev):
                ret.append(ele.val)
                prev=ele
                st.pop()
            else:
                if ele.right: st.append(ele.right)
                if ele.left: st.append(ele.left)

        return ret

Solution().postorderTraversal(TreeNode(1))
