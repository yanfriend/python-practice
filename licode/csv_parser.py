def csv_parser(line):
    line = line + ','
    ans = []

    curr = ''
    i = 0

    while i < len(line):
        if line[i] == '\'':
            qstart = i
            while line[i + 1] == '\'':  # no i<len(line) for append ,
                i += 1
            qblock = line[qstart:i + 1]
            next_ind = line.find(qblock, i + 1)
            curr = line[qstart + 1:next_ind + len(qblock) - 1]
            i = next_ind + len(qblock);
            continue
        if line[i] == ',':
            ans.append(curr)
            curr = ''
        else:
            curr += line[i]
        i += 1

    return '|'.join(ans)

print csv_parser('name,address,any')
print csv_parser('\'john,add,coma\',address,any')
print csv_parser('\'\'john,add,coma\'\',address,any')
print csv_parser('address,any,\'john,add,coma\'')
