class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        sb=['']*numRows
        i=0
        while i<len(s):
            for j in range(numRows):
                if i<len(s):
                    sb[j]+=s[i]
                    i+=1
                else:
                    break
            for j in range(numRows-2,0,-1):
                if i<len(s):
                    sb[j]+=s[i]
                    i+=1
                else:
                    break
        ret=''.join(sb)
        return ret

print Solution().convert('ABC',2)



'''
Total Accepted: 151933
Total Submissions: 571980
Difficulty: Medium
Contributor: LeetCode
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question.
'''
