def factor_number(n):
    ans = []

    def helper(n, start, path):
        if start <= n and len(path) >= 1:
            ans.append(path + [n])

        for k in range(start, n / 2 + 1):
            if n % k == 0:
                helper(n / k, k, path + [k])

    helper(n, 2, [])
    return ans


print factor_number(12)
print factor_number(32)
print factor_number(9)

