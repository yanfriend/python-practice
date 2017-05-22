class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        my_s = S.upper().replace('-', '')
        first_len = len(my_s) % K
        ret_list = []

        if first_len != 0:
            ret_list.append(my_s[0:first_len])

        while first_len < len(my_s):
            ret_list.append(my_s[first_len:first_len + K])
            first_len += K
        return '-'.join(ret_list)

# looks ok, but not run locally
