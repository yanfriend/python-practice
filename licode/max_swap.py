import collections
import string


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str=str(num)
        digit_ind_mp=collections.defaultdict(int)
        for i in range(len(num_str)):
            digit_ind_mp[num_str[i]]=i  # log last one

        str_list=list(num_str)
        for i in range(len(num_str)):
            for ch in string.digits[::-1]:  # from '9' to '0'
                if ch>num_str[i] and digit_ind_mp[ch]>i: # larger digit behind
                    str_list[i],str_list[digit_ind_mp[ch]]=ch,str_list[i]
                    return int(''.join(str_list))
        return num

print Solution().maximumSwap(10909091)
