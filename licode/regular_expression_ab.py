"""
Regular Expression

Implement a simple regex parser which, given a string and a pattern, returns a boolean indicating whether the input matches the pattern.

By simple, we mean that the regex can only contain special character:

    * (star) The star means what you'd expect, that there will be zero or more of previous character in that place in the pattern.
    . (dot) The dot means any character for that position.
    + (plus). The plus means one or more of previous character in that place in the pattern.
"""

def regular_expression(s,p):
    dp=[[False]*(len(s)+1) for _ in range(len(p)+1)]
    dp[0][0]=True
    for i in range(1,len(p)+1):
        if p[i-1]=='*':
            dp[i][0]=dp[i-2][0]

    for i in range(1,len(p)+1):
        for j in range(1, len(s)+1):
            if p[i-1]==s[j-1] or p[i-1]=='.':
                dp[i][j]=dp[i-1][j-1]
            elif p[i-1]=='*':
                dp[i][j]=dp[i-2][j] \
                         or dp[i][j-1] and (s[j-1]==p[i-2] or p[i-2]=='.')
            elif p[i-1]=='+':
                dp[i][j]=dp[i-1][j] and (p[i-2]==s[j-1] or p[i-1]=='.') \
                         or dp[i][j-1] and (p[i-2]==s[j-1] or p[i-1]=='.')
                # first line: match one. a+ <> a
                # second line: match as one letter less in s

    return dp[len(p)][len(s)]

# print regular_expression('abc','a*bc') # true
# print regular_expression(s = "aab", p = "c*a*b") # true
# print regular_expression(s = "mississippi", p = "mis*is*p*.") # false
# print regular_expression(s = "ab", p = ".*") # should be true
# print regular_expression(s = "aa", p = "a*") # true
# print regular_expression(s = "aa", p = "a") # false

print regular_expression("saaaa", "s+a*")  # t
print regular_expression("saaaa", "s+b*") # f
print regular_expression("saaaab", "s+a*") # f
print regular_expression("saaaab", "s+b*") # f
