def dfs(p, s, i, j, mp1, st):
    if i==len(p) and j==len(s): return True
    if i==len(p) or j==len(s): return False

    if p[i] in mp1:
        if s[j:].startswith(mp1[p[i]]):
            return dfs(p, s, i + 1, j + len(mp1[p[i]]), mp1, st)
        else: return False
    else:
        for k in range(j,len(s)):
            if s[j:k+1] in st: continue
            mp1[p[i]]= s[j:k + 1]; st.add(s[j:k+1])
            if dfs(p, s, i+1, k+1, mp1, st): return True
            del mp1[p[i]]; st.remove(s[j:k+1])
    return False

def word_patter_2(pattern,string):
    mp1={}
    st=set()
    return dfs(pattern,string,0,0,mp1,st)

print word_patter_2('ab','cc') # this should be False!

print word_patter_2('abab','redblueredblue') # true
print word_patter_2('aabb','xyzabcxzyabc') # false
print word_patter_2('aabb', 'xyzabcxzyabc') # false
