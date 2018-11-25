import util

def populate(st):
    if not st:
        return

    tmp=st.pop()
    tmp=tmp.right
    while tmp:
        st.append(tmp)
        tmp=tmp.left

def merge_tree(l1,l2):
    ret=[]
    st1=[]; st2=[]

    while l1:
        st1.append(l1)
        l1=l1.left
    while l2:
        st2.append(l2)
        l2=l2.left

    while st1 and st2:
        if st1[-1].val < st2[-1].val:
            ret.append(st1[-1].val); populate(st1)
        else:
            ret.append(st2[-1].val); populate(st2)

    st=st1 or st2
    while st:
        ret.append(st[-1].val); populate(st)

    return ret


r2 = util.TreeNode(21)
r2.right = util.TreeNode(31)
r2.right.right = util.TreeNode(41)

print merge_tree(util.root, r2)
