
def panation(lines, k):
    ret=[]

    while len(lines)>0:
        page = []
        visited = set()
        indices = []
        full_page=False

        for ind,line in enumerate(lines):
            id = int(line.split(',')[0])
            if id not in visited:
                page.append(line)
                visited.add(id)
                indices.append(ind)
                if len(page)==k:
                    full_page=True
                    break

        for i in indices[::-1]:
            del lines[i]
        indices=[]

        if not full_page:  # page not full
            for ind, line in enumerate(lines):
                id = int(line.split(',')[0])
                page.append(line)
                # visited.add(id)
                indices.append(ind)
                if len(page) == k:
                    break
            for i in indices[::-1]:
                del lines[i]

        ret.append(page)

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

print panation(lines,k=5)

"""
output
1,28,310.6,SF
4,5,204.1,SF
20,7,203.2,Oakland
6,8,202.2,SF
7,20,180.1,SF 

6,10,199.1,SF 
1,16,190.4,SF 
2,18,161.2,SF
3,76,146.2,SF
6,29,185.2,SF  -- has to

6,21,162.1,SF
2,30,149.1,SF
2,14,141.1,San Jose. From 1point 3acres bbs
"""


input=['1','2','1','3','4','5','6']
print panation(input, 3)
#
input=['1','1','1','1','1','1','1']
print panation(input, 3)
#
#
input=['1','2','3','4','1','5',
       '1','2','3','1','3']
print panation(input, 5) # new one: 12345, 12311, 3;  # 12345,12313,1
