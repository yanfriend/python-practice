class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1=version1.split('.')
        arr2=version2.split('.')
        if len(arr1)==1: arr1.append('0')
        if len(arr2)==1: arr2.append('0')

        ret=self.my_cmp(arr1[0],arr2[0])

        if ret==0: return cmp(arr1[1],arr2[1])
        else: return ret

    def my_cmp(self,s1,s2):
        import ipdb;ipdb.set_trace()

        n1=int(s1)
        n2=int(s2)
        if n1>n2: return 1
        elif n1<n2: return -1
        else: return 0

print Solution().compareVersion('01','1')
