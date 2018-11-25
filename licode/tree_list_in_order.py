class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def tree_to_list_in_order(root):
    h,t=tl_helper(root)
    return h

def tl_helper(root):
    if not root: return None,None

    lh,lt=tl_helper(root.left)
    rh,rt=tl_helper(root.right)

    root.left=lt
    if lt: lt.right=root
    else: lh=lt=root

    root.right=rh
    if rh: rh.left=root
    else: lt=rt=root

    return lh,rt


# below for testing
root=TreeNode(10)
root.left=TreeNode(5)
root.left.left=TreeNode(4)
root.left.right=TreeNode(8)
root.right=TreeNode(15)
root.right.left=TreeNode(14)
root.right.right=TreeNode(18)

node=tree_to_list_in_order(root)

# print node
prev=None
while node:  # print asceding order
    print node.val,
    prev=node
    node=node.right
print
while prev: # print descending order
    print prev.val,
    prev=prev.left
