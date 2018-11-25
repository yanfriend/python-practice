pre=[10,8,5,9,15,16]

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=self.right=None

def pre_to_tree(pre):
    if not pre: return None
    root=TreeNode(pre[0])
    st=[root]

    for i in range(1,len(pre)):
        tmp=None
        while st and pre[i]>st[-1].val:  # st is increasing
            tmp=st.pop()
        if tmp is None:
            st[-1].left=TreeNode(pre[i])
            st.append(st[-1].left)
        else:
            tmp.right=TreeNode(pre[i])
            st.append(tmp.right)
    return root

def inorder(root):
    if not root: return
    inorder(root.left)
    print root.val,
    inorder(root.right)

root=pre_to_tree(pre)
inorder(root)

"""
% python pre_to_bst.py
5 8 9 10 15 16
"""
