def find_perm(s):
    n = len(s)
    ans = [i + 1 for i in range(n + 1)]  # 1..n+1

    i = 0
    while i < n:
        if s[i] == 'I': i += 1; continue
        start = i
        while s[i] == 'D':
            i += 1
        ans[start:i + 1] = ans[start:i + 1][::-1]
    return ans


assert find_perm('DI'), [2, 1, 3]

print find_perm('DDIIDI')


"""
Input: "DI"
Output: [2,1,3]

DDIIDI
321 4 65 7
"""
