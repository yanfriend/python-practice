
def palin_pairs(words):
    def is_palin(w):
        return w==w[::-1]

    m={w:i for i,w in enumerate(words)}
    ret=[]

    for i, w in enumerate(words):
        for j in range(len(w)+1):
            if is_palin(w[j:]) and w[:j][::-1] in m and m[w[:j][::-1]]!=i and j!=len(w):
                ret.append((i, m[w[:j][::-1]]))

            if is_palin(w[:j]) and w[j:][::-1] in m and m[w[j:][::-1]]!=i:
                ret.append((m[w[j:][::-1]],i))

    return ret

# print palin_pairs(['abb','bba','a', 'aba'])
# print palin_pairs(["a",""])
print palin_pairs(["abcd","dcba","lls","s","sssll"])


'''
two edge cases below:

Input:  both need to cut out empty string '', so len(w)+1 
["a",""]
Output:
[[0,1]]
Expected:
[[0,1],[1,0]]

Input:
["abcd","dcba","lls","s","sssll"]
Output:
[[1,0],[0,1],[0,1],[1,0],[3,2],[2,4]]
Expected:
[[0,1],[1,0],[3,2],[2,4]]
'''
