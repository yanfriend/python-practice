import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        ch_dict = collections.defaultdict(int)
        start = 0
        ret = ''

        for i, ch in enumerate(s):
            ch_dict[ch] += 1

            if len(ch_dict) > 2:  # move start
                while start < i:
                    ch_dict[s[start]] -= 1
                    if ch_dict[s[start]] == 0:
                        del ch_dict[s[start]]
                        start += 1
                        break
                    start += 1

            if i - start + 1 > len(ret):
                ret = s[start:i + 1]
        return ret

print Solution().lengthOfLongestSubstringTwoDistinct('abcbbbbcccbdddadacb')
print Solution().lengthOfLongestSubstringTwoDistinct('aaaabbbbcc')



# class Solution(object):
#     def lengthOfLongestSubstringTwoDistinct(self, s):
#         ch_dict = {}
#         cnt = 0
#         start = 0
#         ret = ''
#
#         for i, ch in enumerate(s):
#             if ch not in ch_dict:
#                 ch_dict[ch] = 1
#                 cnt += 1
#             else:
#                 ch_dict[ch] += 1
#
#             if cnt > 2:  # move start
#                 while start < i:
#                     if s[start] in ch_dict:
#                         ch_dict[s[start]] -= 1
#                         if ch_dict[s[start]] == 0:
#                             del ch_dict[s[start]]
#                             cnt -= 1
#                             start += 1
#                             break
#                     start += 1
#
#             if i - start + 1 > len(ret):
#                 ret = s[start:i + 1]
#         return ret
#
#
# print Solution().lengthOfLongestSubstringTwoDistinct('abcbbbbcccbdddadacb')
# print Solution().lengthOfLongestSubstringTwoDistinct('aaaabbbbcc')
