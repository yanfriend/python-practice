class Solution(object):
    def longestConsecutive(self,root):
        ans=[0]
        self.helper(root,root,ans)
        return ans[0]

    def helper(self, root, parent, ans):
        if not root: return (0,0) # inc count, des count

        l=self.helper(root.left, root, ans)
        r=self.helper(root.right, root, ans)

        ans[0]=max(ans,
                   l[0] + r[1] + 1,  # if not continuous, l0,1, r0,1 are all 0
                   l[1] + r[0] + 1)

        inc=des=0
        if root.val==parent.val+1: # inc
            inc=max(l[0],r[0])+1
        elif root.val==parent.val-1: # desc
            des=max(l[1],r[1])+1
        return inc,des

