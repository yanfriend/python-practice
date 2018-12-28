def is_palin(word):
    return word == word[::-1]


def mini_palindra(word):
    n = len(word)
    dp = [i for i in range(n)]
    dp.append(n)  # 0..n

    for i in range(1, n + 1):
        for j in range(0, i):
            if is_palin(word[j:i]):
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]

    # also, can dp to calc if word[i:j] is palindra. running complexity square n.


print mini_palindra('aaa')  # 1
print mini_palindra('aaab')  # 2
print mini_palindra('abc')  # 3

print mini_palindra('abccba')  # 1
print mini_palindra('abccbadd')  # 2
