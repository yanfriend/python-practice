def countDigitOne(n):
                if n <= 0:
                    return 0
                q, x, ans = n, 1, 0
                while q > 0:
                    digit = q % 10
                    q /= 10
                    ans += q * x
                    if digit == 1:
                        ans += n % x + 1
                    elif digit > 1:
                        ans += x
                    x *= 10

                    print ans

                return ans

# print countDigitOne(13)
# print countDigitOne(101)

print countDigitOne(102)