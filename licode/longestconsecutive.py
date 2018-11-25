import util

def longest_consecutive(root):
    ret=[0]
    helper(ret, root, root)
    return ret[0]

def helper(ret, node, parent):
    if not node: return 0,0

    l=helper(ret, node.left, node)
    r=helper(ret, node.right, node)

    ti,td=0,0
    if node.val+1==parent.val: # inc
        ti=max(l[0],r[0])+1
    elif node.val-1==parent.val: # dec
        td=max(l[1],r[1])+1

    ret[0]=max(ret[0],l[0]+r[1]+1,l[1]+r[0]+1)

    return ti, td

root=util.TreeNode(5)
root.left=util.TreeNode(4)
root.left.right=util.TreeNode(3)
root.left.left=util.TreeNode(2)

root.right=util.TreeNode(6)
root.right.right=util.TreeNode(4)

print longest_consecutive(root) # 4

