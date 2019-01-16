import collections

def panation(lines):

    i=0; n=len(lines)
    pages=[]

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
                if len(page)==5:
                    full_page=True
                    break

        if full_page:
            pages.append(page)
            for i in indices[::-1]:
                del lines[i]
        else: # page not full
            if len(lines)>0:
                for ind, line in enumerate(lines):
                    id = int(line.split(',')[0])
                    page.append(line)
                    visited.add(id)
                    indices.append(ind)
                    if len(page) == 5:
                        full_page = True
                        break
                if full_page:
                    pages.append(page)
                for i in sorted(indices)[::-1]:
                    del lines[i]

    return pages


def panation_id_to_page(lines): # need to sort if page size<5
    id_to_page={}
    pages=collections.defaultdict(list)
    curr_page_id=0

    for line in lines:
        id=int(line.split(',')[0])
        last_id=id_to_page.get(id,-1)

        new_id = max(last_id+1, curr_page_id)

        id_to_page[id] = new_id
        pages[new_id].append(line)

        if len(pages[curr_page_id])==5:
            curr_page_id+=1

    num=0
    for i in range(max(pages)+1):
        page_lines=pages[i]
        for l in page_lines:
            print l
            num+=1
            if num%5==0:
                print ''

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

panation(lines)

"""
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
