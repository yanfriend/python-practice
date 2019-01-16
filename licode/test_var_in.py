class Solution(object):
    def fun1(self):
        var1=2
        self.fun2(var1)
        print var1

    def fun2(self,var):
        var=10

    def ts(self,s):
        s=s+'='
        print s

print Solution().fun1() # int value cant be changed in func

s=Solution()
word='abc'
s.ts(word)
print word # word is not changed. now still abc
