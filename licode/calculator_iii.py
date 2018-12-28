
def calculate(s):
    ans=0
    curr_res=0
    op='+'
    num=0

    i=0
    while i<len(s):
        ch=s[i]
        if ch.isdigit():
            while i<len(s) and s[i].isdigit():
                num=num*10 + int(s[i])
                i+=1
            i-=1
        elif ch=='(':
            cnt=1; i+=1; start=i
            while cnt!=0:
                if s[i]=='(': cnt+=1
                elif s[i]==')': cnt-=1
                i+=1
            num=calculate(s[start:i-1])
            i-=1
        if ch in '+-*/' or i==len(s)-1: # use ch, not elif s[i], because last num need to do below work too.
            if op=='+': curr_res += num
            elif op=='-': curr_res -= num
            elif op=='*': curr_res *= num
            elif op=='/': curr_res /= num

            if ch in '+-' or i==len(s)-1:
                ans+=curr_res
                curr_res=0

            op=ch; num=0
        i+=1
    return ans

# run in brain '6-4/2'

print calculate("1 + 1") # 2
print calculate(" 6-4 / 2 ")  # 4
print calculate("2*(5+5*2)/3+(6/2+8)") # 21
print calculate("(2+6* 3+5- (3*14/7+2)*5)+3") # -12
print calculate('1+12/6*2') # 5