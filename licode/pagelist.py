
class Solution(object):
    def pagelist(self, csv_lines, k):
        """
        seperate to diff pages, and print by page
        :param csv_lines:
        :param k:
        :return:
        """
        id_to_pageid = {}  # id:page_id
        pages = [] # list of list
        pageid = 0

        for i,id in enumerate(csv_lines):
          if id not in id_to_pageid or id_to_pageid[id]<pageid: # not in or in previous pages
            id_to_pageid[id]=pageid
          if id_to_pageid[id]==len(pages): # new page, append
            pages.append([])
          pages[id_to_pageid[id]].append(csv_lines[i])
          id_to_pageid[id]+=1 # if same id, at this page id
          if len(pages[pageid])==k: # pageid is full
            pageid+=1

        lineid = 0
        for page in pages:
          for line in page:
            if lineid == 0:
              print '===========page============'
            print line
            lineid+=1
            if lineid == k:
                lineid = 0

input=[1,2,1,3,4,5,6]
print Solution().pagelist(input, 3)


input=[1,1,1,1,1,1,1]
print Solution().pagelist(input, 3)


input=[1,2,3,4,1,5,1,2,3,1,3]
print Solution().pagelist(input, 5) # 12345,12313,1
