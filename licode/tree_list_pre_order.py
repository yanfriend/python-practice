class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def tree_to_list_pre_order(root):
    h,t=helper(root)
    # return h

def helper(root):
        if not root: return None, None

        lh,lt=helper(root.left)
        rh,rt=helper(root.right)

        root.left=None

        curr=root
        if lh:
            curr.right=lh
            curr=lt
        else: lh=root
        if rh:
            curr.right=rh
        else:
            rt=curr

        return root,rt


# below for testing
root=TreeNode(10)
root.left=TreeNode(5)
root.left.left=TreeNode(4)
root.left.right=TreeNode(8)
root.right=TreeNode(15)
root.right.left=TreeNode(14)
root.right.right=TreeNode(18)
"""
   10
  5   15
4  8 14 18
"""
node=tree_to_list_pre_order(root)
node=root  # root has been changed.

# print node
prev=None
while node:
    print node.val,
    prev=node
    node=node.right
print
