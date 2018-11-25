class TreeNode:
    def __init__(self,val):
        self.left=self.right=None
        self.val=val

class Solution(object):

    def str2Tree(self,s):
        if not s: return None

        p_index=s.find('(')
        if p_index==-1: val=int(s); return TreeNode(val)

        val=int(s[:p_index])
        ret=TreeNode(val)

        cnt=0
        for i in range(p_index,len(s)):
            if s[i]=='(': cnt+=1
            elif s[i]==')': cnt-=1

            if cnt==0: # find the corresponding last )
               break

        ret.left=self.str2Tree(s[p_index+1:i])
        ret.right=self.str2Tree(s[i+1+1:-1]) # skip ), next (, ending skip last ). make sure format is N(xxx)
        return ret

def my_print(tree):
    if not tree: return
    my_print(tree.left)
    print tree.val
    my_print(tree.right)

tree=Solution().str2Tree('4(2(3)(1))(6(5))') # there is no empty ()
my_print(tree)

print ''
tree=Solution().str2Tree('5(4(3)(7))(6()(8))') # there is no empty ()
my_print(tree)
