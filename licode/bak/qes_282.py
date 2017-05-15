import copy
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if len(num)==0: return []

        ret=[]
        path=''
        self.helper(ret, path, num, target, 0, 0, 0)
        return ret

    def helper(self,ret, path, num, target, pos, curr_val, prev_val):
        import ipdb; ipdb.set_trace()
        print pos,
        if pos==len(num):
            if curr_val==num: ret.append(copy.deepcopy(path))
            return

        for i in range(pos+1,len(num)+1):
            str=num[pos:i]
            val=int(str)
            if pos==0:
                self.helper(ret, path+str, num, target, i, val, val) # not need path+ ?
            else:
                self.helper(ret, path+'+'+str, num, target, i, curr_val+val, val)
                self.helper(ret, path+'-'+str, num, target, i, curr_val-val, -val)
                self.helper(ret, path+'*'+str, num, target, i, curr_val-prev_val+prev_val*val, prev_val*val)


print Solution().addOperators('123',6)
