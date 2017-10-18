
def comb(s, ret, path, ind):
    if ind==len(s):
        ret.append(path)
        return ret
    comb(s, ret, path+s[ind], ind+1)

    if s[ind].islower():
        comb(s, ret, path+s[ind].upper(), ind+1)

ret=[]
print comb('abC', ret, '', 0)
print ret
