def findn1n2(s):
    ret=set()
    tail=''
    helper(s,ret,tail)
    return list(ret)

def helper(s,ret,tail):
    if 1<=s<=9:
        sn=int(tail) if tail else 0
        ln=int(str(s)+tail)
        ret.add((sn,ln))
        return
    if s<=0: return

    # as last digit missing
    sn=s/11
    ln=s-sn
    if len(str(ln))-len(str(sn))==1:
        ret.add((int(str(sn)+tail),int(str(ln)+tail)))

    if s%2: # odd digit ended.
        return
    # even last digit now

    # divide last digit
    tail1=str((s%10)/2)+tail
    s1=s/10
    helper(s1,ret,tail1)

    # import ipdb;ipdb.set_trace()
    # divide last digit and double it has carrier.
    tmp=(10+s%10)/2
    s=(s-2*tmp)/10
    tail2=str(tmp)+tail
    helper(s,ret,tail2)



# def findn1n2(s):
#     if s < 10: return [(s, 0)]
#     rec = set()
#     base = 1
#
#     while s / (11 * base):
#         h = s / (11 * base)
#         m = s % (11 * base)
#         e = 0
#         while e * base <= m:
#             if (m - e * base) % 2 == 0 and (m - e * base) / 2 < base:
#                 t = (m - e * base) / 2
#                 n1 = h * 10 * base + e * base + t
#                 n2 = h * base + t
#                 rec.add((n1, n2))
#
#             e += 1
#         base *= 10
#     return list(rec)

# def findn1n2(s): # this is gabage!
#     if s < 10: return [(s, 0)]
#     rec = set()
#     r = 0
#     while s / (11 * 10 ** r):
#         h = s / (11 * 10 ** r)
#         m = s % (11 * 10 ** r)
#         e = m / (10 ** r)
#         t = (m % (10 ** r)) / 2
#         n1 = h * 10 ** (r + 1) + e * 10 ** r + t
#         n2 = h * 10 ** r + t
#         rec.add((n1, n2))
#         r += 1
#     return list(rec)

print findn1n2(2) #[(2, 0)]
print findn1n2(39) #[(36, 3)]
print findn1n2(36) #, 33,3; 28,8
print findn1n2(1246) #[(1073, 173), (1133, 113), (1123, 123), (1128, 118)]
print findn1n2(1346) #[(1218, 128), (1173, 173), (1224, 122), (1223, 123)]
