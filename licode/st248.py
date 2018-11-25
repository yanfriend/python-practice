class Solution(object):

    def strobogrammaticInRange(self, low, high):
        ret=0
        ret+=self.range(low,high,'')
        ret+=self.range(low,high,'0')
        ret+=self.range(low,high,'1')
        ret+=self.range(low,high,'8')
        return ret

    def range(self,low,high,path):
        ret=0
        if len(path)>0 and int(low)<=int(path)<=int(high) and (len(path)>1 and path[0]!='0' or len(path)==1): ret+=1
        if len(path)>len(high) or (len(path)>0 and int(path)>int(high)): return ret
        if len(path)+2>len(high): return ret

        ret+=self.range(low,high,'0'+path+'0')
        ret+=self.range(low,high,'1'+path+'1')
        ret+=self.range(low,high,'8'+path+'8')
        ret+=self.range(low,high,'6'+path+'9')
        ret+=self.range(low,high,'9'+path+'6')

        return ret

print Solution().strobogrammaticInRange('50','120') # 50,100, =3; 50,120=5
