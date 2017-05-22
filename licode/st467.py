import collections

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        map=collections.defaultdict(int)
        maxl=0
        for i,ch in enumerate(p):
            if i>0 and ( ord(p[i])-ord(p[i-1])==1 or (p[i-1]=='z' and p[i]=='a')):
                # map[ch]=max(map[ch],map[p[i-1]]+1) # this outputs larger;
                # the point is you cant rely on previous letter.
                # such as 'abcdbcd', that may overcount.
                maxl+=1
            else:
                maxl=1
            map[ch]=max(map[ch],maxl)

        return sum([ val for val in map.values()])


print Solution().findSubstringInWraproundString('abcdbcd') # 1,2,3,4,=10

# "cdefghefghijklmnopqrstuvwxmnijklmnopqrstuvbcdefghijklmnopqrstuvwabcddefghijklfghijklmabcdefghijklmnopqrstuvwxymnopqrstuvwxyz"

