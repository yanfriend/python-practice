def cal1(s):
    st=[]; sign=1; ret=0

    i=0
    while i<len(s):
        ch=s[i]
        if ch.isdigit():
            num=0
            while i<len(s) and s[i].isdigit():
                num=num*10+int(s[i])
                i+=1
            if i<len(s): i-=1
            ret+=sign*num
        elif ch=='+': sign=1
        elif ch=='-': sign=-1
        elif ch=='(':
            st.append(ret)
            st.append(sign)
            ret=0; sign=1
        elif ch==')':
            sign=st.pop()
            ret=st.pop()+sign*ret
            sign=1
        i+=1
    return ret

print cal1('2+(2-3)')
