class Solution(object):
    def fun1(self):
        var1=0
        self.fun2(var1)
        print var1

    def fun2(self,var):
        var=10

print Solution().fun1()
