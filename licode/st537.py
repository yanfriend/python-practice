class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alist=a.replace('i','').split('+')
        blist=b.replace('i','').split('+')

        ret_a=int(alist[0])*int(blist[0]) - int(alist[1])*int(blist[1])
        ret_b=int(alist[0])*int(blist[1]) + int(alist[1])*int(blist[0])

        return str(ret_a)+'+'+str(ret_b)+'i'
