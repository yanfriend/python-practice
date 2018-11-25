def strstr(s,p):
    if not s or not p: return -1

    for i in range(len(s)-len(p)+1):
        if s[i:i+len(p)]==p: return i
    return -1


# def strstr(s,p):
#     if not s or not p: return -1
#
#     for i in range(len(s)-len(p)+1):
#         not_match=False
#         for j in range(len(p)):
#             if s[i+j]==p[j]: continue
#             not_match=True
#         # import ipdb; ipdb.set_trace()
#         if not not_match: return i
#     return -1


print strstr('ab','a')
print strstr('abc','bc')
print strstr('abc','bd')

