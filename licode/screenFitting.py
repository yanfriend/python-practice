"""
Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
Output:
2

a-bcd-
e-a---
bcd-e-


"""


class Solution(object):
    def screen_fitting(self, row, col, words):
        sentence = ' '.join(words) + ' '

        start=0
        for i in range(row):
            start+=col
            pos = start%len(sentence)
            if sentence[pos]==' ': start+=1  # start to after non-space
            else:
                while start>0 and sentence[(start-1)%len(sentence)]!=' ': start-=1 # start to after non-space
        return start/len(sentence)


print Solution().screen_fitting(3, 6, ['a', 'bad', 'e'])  # 2

print Solution().screen_fitting(4, 5, ["I", "had", "apple", "pie"])  # 1

print Solution().screen_fitting(2, 8, ['hello', 'world'])  # 1, len: 11

