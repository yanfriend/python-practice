def parse(line):
    ret = []
    in_quote = False

    field = ''
    for i in range(len(line)):
        ch = line[i]
        if in_quote:
            if ch == '\"':
                if i + 1 < len(line) and line[i + 1] == '\"':
                    field += '\"'
                    i += 1
                else:
                    in_quote = False
            else:
                field += ch
        else:
            if ch == '\"':
                in_quote = True
            elif ch == ',':
                ret.append(field)
                field = ''
            else:
                field += ch
    if field:
        ret.append(field)

    return '|'.join(ret)


print parse('aa,bb,\"aa\",\"aa,bb\",\"aa\"\"aa\"\"\"')
# aa|bb|aa|aa,bb|aa"aa"

print parse('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1 """Alexandra Alex"""')
# ans: Alexandra "Alex"|Menendez|alex.menendez@gmail.com|Miami|1 "Alexandra Alex"
