def numDupDigitsAtMostN(N):
    L = map(int, str(N + 1))
    res, n = 0, len(L)

    def A(m, n):
        return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

    for i in range(1, n):
        res += 9 * A(9, i - 1) # n-1 digits, all number w/t dup
        # print 'init:',i,res
    print res

    s = set()
    for i, x in enumerate(L):
        print 'enumerate(L)', i, x
        for y in range(0 if i else 1, x):
            if y not in s:  # 87 .. 7 again. avoid

                # print A(9 - i, n - i - 1)
                # print 'y,i,A:', y,i,A(9 - i, n - i - 1)  # 9*8*7 for i==0; 8*7 for i==1;
                res += A(9 - i, n - i - 1)

            else: print 'dup:', y
        print i,x, res

        if x in s:
            print 'in break:',x
            break

        s.add(x)
    return N - res

# print numDupDigitsAtMostN(10)
# print numDupDigitsAtMostN(11)

print numDupDigitsAtMostN(8765)
