
def pagination(lines, k):
    ret=[]
    while len(lines)>0:
        visited=set()
        to_delete=[]
        one_page=[]
        full=False
        for i, l in enumerate(lines):
            id = int(lines[i].split(',')[0])
            if id not in visited:
                one_page.append(l)
                to_delete.append(i)
                visited.add(id)
                if len(one_page)==k:
                    full=True
                    break
        for i in to_delete[::-1]:
            del lines[i]
        to_delete=[]

        if not full:
            for i, l in enumerate(lines):
                one_page.append(l)
                to_delete.append(i)
                if len(one_page) == k:
                    break
            for i in to_delete[::-1]:
                del lines[i]

        ret.append(one_page)

    return ret

lines=[
"1,28,310.6,SF",
"4,5,204.1,SF",
"20,7,203.2,Oakland",
"6,8,202.2,SF",
"6,10,199.1,SF",
"1,16,190.4,SF",
"6,29,185.2,SF",
"7,20,180.1,SF",
"6,21,162.1,SF",
"2,18,161.2,SF",
"2,30,149.1,SF",
"3,76,146.2,SF",
"2,14,141.1,San Jose",
]
print pagination(lines,k=5)
