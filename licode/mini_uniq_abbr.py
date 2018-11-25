import Queue

def generate_all(word):
    """
    :type word: string
    :rtype: priority queue of (lenth, word variation)
    """
    pq=Queue.PriorityQueue()

    for i in range(2**len(word)):
        size=0; cnt=0; aword=''
        for j in range(len(word)):
            if i>>j&1: # 1
                cnt+=1
            else:
                if cnt>0:
                    aword+=str(cnt)
                    size+=1
                    cnt=0
                aword+=word[j]
                size+=1
        if cnt>0: # if ending number
            size+=1
            aword+=str(cnt)
        pq.put((size,aword))

    return pq


def valid(word, abbr):
    # check if abbr is valid for word
    i=0; j=0
    while i<len(word) and j<len(abbr):
        if abbr[j].isalpha():
            if word[i]==abbr[j]: i+=1; j+=1; continue
            else: return False
        else:
            cnt=0
            while j<len(abbr) and abbr[j].isdigit():
                if cnt == 0 and abbr[j] == '0': return False
                cnt=cnt*10+int(abbr[j])
                j+=1
            i+=cnt
    return i==len(word) and j==len(abbr)


def minAbbreviation(target, words):
    pq=generate_all(target)
    while not pq.empty():
        abbr=pq.get()[1]
        if all(not valid(word, abbr) for word in words):
            return abbr
    return ''

#
# pq=generate_all('word')
# while not pq.empty():
#     tmp=pq.get()[1]
#     print tmp, valid('word',tmp)
# # 4 3d w3 1o2 2r1 2rd w2d wo2 1o1d 1or1 1ord w1r1 w1rd wo1d wor1 word

print minAbbreviation("apple", ["blade"]) # a4
print minAbbreviation('apple', ['plain', 'amber', 'blade']) # 1p3
