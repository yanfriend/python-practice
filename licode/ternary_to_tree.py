import util

def convertExpression(exp,i):
    st=[]
    ltree=rtree=None
    for ch in reversed(exp):
        if ch.isalpha():
            st.append(util.TreeNode(ch))
            st[-1].left=ltree
            st[-1].right=rtree
            ltree=rtree=None
        elif ch=='?':
            ltree=st.pop()
            rtree=st.pop()
    return st[-1]

exp='a?c:d?e:f'
root=convertExpression(exp,0)
util.pre_print(root)

print

exp2='a?b?c:d:f'
root=convertExpression(exp2,0)
util.pre_print(root)
