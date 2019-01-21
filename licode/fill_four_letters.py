def fill_four_letter():
    # this is to simulate guess a number, after getting all four digits.
    # and reduce test call.
    bad_dg = 1
    digits = [3, 4, 5, 6]
    ans = [bad_dg] * 4
    cnt = 0

    secret = [6, 4, 5, 3]

    def test(word):
        ans = 0
        for i in range(4):
            if word[i] == secret[i]: ans += 1
        return ans

    for ind, letter in enumerate(digits):
        for i in range(4):
            if ans[i] != bad_dg: continue
            ans[i] = letter
            if i == 4 - ind - 1: break
            if test(ans) == ind + 1:
                cnt += 1
                break
            else:
                ans[i] = bad_dg

    return ans, cnt

print fill_four_letter()
