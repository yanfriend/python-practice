class NestedInteger(object):
    def __init__(self, obj=None):
        print obj

    def add(self, nestedInteger):
        print nestedInteger

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        arr=s.split(',')
        if arr[0].startswith('['):
            node,_ = self.parseList(arr,0)
        else:
            node,_= self.parseInt(arr,0)
        return node

    def parseList(self,arr,ind):
        ret=NestedInteger()
        arr[ind]=arr[ind][1:] # remove first [
        i=ind
        while i<len(arr):
            import ipdb; ipdb.set_trace()

            if arr[i].startswith('['):
                node, i = self.parseList(arr,i)
                ret.add(node)
            elif arr[i][0] in '-0123456789':
                node, i=self.parseInt(arr,i)
                ret.add(node)
            elif arr[i].startswith(']'):
                arr[i]=arr[i][1:] # get rid of ]
                if arr[i]=='':
                    i += 1
                return ret, i
        return ret, ind

    def parseInt(self,arr,ind):
        # ret=NestedInteger()
        pos=arr[ind].rfind(']')
        if pos>=0:
            tmp=arr[ind]
            ret=NestedInteger(int(tmp.replace(']','')))
            arr[ind]=arr[ind][pos:]
        else:
            ret=NestedInteger(int(arr[ind]))
            arr[ind]=''
            ind += 1
        return ret, ind

print Solution().deserialize('[-1,-2]')
