class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l1_dict={}
        for i,val in enumerate(list1):
            l1_dict[val]=i

        max_sum=float('inf')
        ret=[]

        for i,val in enumerate(list2):
            if val in l1_dict:
                if i+l1_dict[val]<max_sum:
                    max_sum=i+l1_dict[val]
                    ret=[val]
                elif i+l1_dict[val]==max_sum:
                    ret.append(val)
        return ret
