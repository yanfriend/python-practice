

def next_iterators(words):
    n=len(words)
    indexes=[0]*n

    ret=[]
    while indexes[0]<len(words[0]):
        ele=[]
        for i,ind in enumerate(indexes):
            ele.append(words[i][ind])
        ret.append(''.join(ele))

        i=n-1
        indexes[i]+=1
        while i>0 and indexes[i]==len(words[i]):
            indexes[i]=0
            indexes[i-1]+=1
            i-=1
    return ret

words=next_iterators(['hello', 'world', 'java'])
print len(words), words # 100 length

