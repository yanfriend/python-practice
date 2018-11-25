class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_val=str(n)
        found=False
        for i in range(len(str_val)-1,0,-1):
            if str_val[i]>str_val[i-1]:
                found = True
                break
        if not found: return -1

        # find smallest letter after i-1
        latter=str_val[i:]
        ch=min(latter)

        ret=str_val[:i-1]+ch
        latter=''.join(sorted(str_val[i:].replace(ch,str_val[i-1],1)))
        return int(ret+latter)

print Solution().nextGreaterElement(21)
