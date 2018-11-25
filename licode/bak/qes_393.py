class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for num in data:
            if count == 0:
                if num & 0x80 == 0: continue # 0xxx xxxx
                elif num & 0xe0 == 0xc0: count = 1  # 110x xxxx
                elif num & 0xf0 == 0xe0: count = 2 # 1110 xxxx
                elif num & 0xf8 == 0xf0: count = 3 # 1111 0xxx
                else: return False
            else:
                count -= 1
                if num & 0xc0 != 0x80:  return False
        return count == 0

print Solution().validUtf8([1, 3, 9])
