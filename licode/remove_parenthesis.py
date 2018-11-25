class Solution(object):
    def dfs(self, s, ch, last_i, last_j):
        cnt=0
        for i in range(last_i,len(s)):
            if s[i] in ('(',')'):
                cnt=cnt+1 if s[i]==ch else cnt-1
            if cnt<=0: continue # valid.

            for j in range(last_j, i+1): # first round, more ')' till index i
                if s[j]==ch and (j==last_j or s[j-1]!=ch): # if continous ch, only remove the leftmoset one.
                    self.dfs(s[:j]+s[j+1:],ch,i,j) # remove ) at index j
            return # return as remaining has preocess by recursion

        s=s[::-1]
        if ch==')': return self.dfs(s,'(',0,0) # do second round
        self.ret.append(s) # add at the end.

    def removeInvalidParentheses(self,s):
        self.ret=[]
        self.dfs(s, ')',0,0)
        return self.ret

print Solution().removeInvalidParentheses('()())()')
print Solution().removeInvalidParentheses('(a)())()')
print Solution().removeInvalidParentheses(')(')

# n*k running time; k is number of valid strings

# The program only generates valid answers. Every path in the search generates one valid answer.
# The whole search space is a tree with k leaves. The number of nodes in the tree is roughly O(k).
# But this is not always true, for example a degenerated tree.
#
# To generate one node it requires O(n) time from the string concatenation among other things.
# So roughly O(nk). Accurately O(nm) where m is the total "number of recursive calls" or "nodes in the search tree".
# Then you need to relate m to n in the worst case.

