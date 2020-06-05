def countDigitLess(d, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0: return 0
    head, multiplier, ret = n, 1, 0
    while head > 0:    # the num is formatted like: head, mod, muliplier
        digit = head % 10
        head /= 10
        ret += head * multiplier
        if digit == d:
            ret += n % multiplier + 1
        elif digit > d:
            ret += multiplier
        multiplier *= 10
    return ret


def digitsCount(d, low, high):
    return countDigitLess(d, high) - countDigitLess(d, low - 1)


print digitsCount(d=1, low=1, high=13)  # 6
print digitsCount(d=3, low=100, high=250)  # 35
