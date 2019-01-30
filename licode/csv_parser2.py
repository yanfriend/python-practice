
def parse(s):
    in_quote=False

    curr=''
    ret=[]
    for i in range(len(s)):
        ch=s[i]
        if in_quote:
            if ch=='\"':
                if i+1<len(s) and s[i+1]=='\"':
                    curr+='\"'; i+=1
                else:
                    in_quote=False
            else:
                curr+=ch
        else:
            if ch=='\"':
                in_quote=True
            elif ch==',':
                ret.append(curr)
                curr=''
            else:
                curr+=ch
    if curr: ret.append(curr)
    return '|'.join(ret)


def parse_split(s):
    fields = s.split(',') # for one line.

    ret=[]

    start=-1
    for i,f in enumerate(fields):
        cnt=f.count('\"')
        if cnt%2==0:
            ret.append(f)
        else:
            if start==-1:
                start=i
            else:
                ret.append(','.join(fields[start:i+1]))
                start=i+1

    return ret




print parse_split('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1 """Alexandra Alex"""')
# ['"Alexandra ""Alex"""', 'Menendez', 'alex.menendez@gmail.com', 'Miami', '1 """Alexandra Alex"""'] first step


print parse('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1 """Alexandra Alex"""')
# ans: Alexandra "Alex"|Menendez|alex.menendez@gmail.com|Miami|1 "Alexandra Alex"

print parse('aa,bb,\"aa\",\"aa,bb\",\"aa\"\"aa\"\"\"')
# ans: aa|bb|aa|aa,bb|aa"aa"
