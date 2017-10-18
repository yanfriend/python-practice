def cal2_simple(s):
    s=s.replace(' ','')
    ret=0; prev=0 # if +-, meet to ret; if meet */, to prev
    sign=1; op=-1

    i=0
    while i<len(s):
        if s[i].isdigit():
            num=0
            while i<len(s) and s[i].isdigit():
                num=num*10+int(s[i])
                i+=1
            if i<len(s): i-=1

            if op==0: # sign does not work for *, /, only for +, -, always set to prev
                prev=prev*num
                op=-1
            elif op==1:
                prev=prev/num
                op=-1
            else:
                prev=num
        elif s[i]=='+':
            ret+=sign*prev
            sign=1
        elif s[i]=='-':
            ret+=sign*prev
            sign=-1
        elif s[i]=='*': op=0
        elif s[i]=='/': op=1

        i+=1

    return ret+sign*prev

# more school traditional.
def cal2(s):
    s=s.replace(' ','')

    pres={}
    pres['+']=pres['-']=1
    pres['*']=pres['/']=2

    st_num=[]; st_op=[]
    i=0
    while i<len(s):
        if s[i].isdigit():
            num=0
            while i<len(s) and s[i].isdigit():
                num=num*10+int(s[i])
                i+=1
            st_num.append(num)
            if i<len(s): i-=1
        elif s[i] in ('+','-','*','/'):
            if len(st_op)>0 and pres[st_op[-1]]>=pres[s[i]]:
                while len(st_op)>0:
                    if pres[st_op[-1]] >= pres[s[i]]:
                        st_num.append(
                            cal_num(st_op.pop(),st_num.pop(),st_num.pop())
                        )
                    else: break
            st_op.append(s[i])
        i+=1

    while len(st_op) > 0:
        st_num.append(
            cal_num(st_op.pop(), st_num.pop(), st_num.pop())
        )
    return st_num[-1]

def cal_num(op, num2, num1):
    if op=='+': return num1+num2
    elif op=='-': return num1-num2
    elif op=='*': return num1*num2
    elif op=='/': return num1//num2
    else: return 0


print cal2('3+4/2*5')  # 13
print cal2(('6-4/2'))  # 4
