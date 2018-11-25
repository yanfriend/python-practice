def str_encoding(s):
    ret=''
    if not s: return ret

    cnt=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cnt+=1
        else:
            ret+=str(cnt)+s[i-1]
            cnt=1
    ret+=str(cnt)+s[-1]
    return ret

print str_encoding('aaabbc')  # 3a2b1c

