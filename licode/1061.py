def equivalent(A,B,S):
    n=len(A)
    parent={}

    def find(a):
        if a not in parent:
            parent[a]=a
        if a!=parent[a]:
            parent[a]=find(parent[a])
        return parent[a]

    def update(a,b):
        parenta = find(a)
        parentb = find(b)
        if parenta<parentb:
            parent[parentb]=parenta
        else:
            parent[parenta]=parentb

    for i in range(n):
        update(A[i],B[i])

    ret=[]
    for s in S:
        ret.append(find(s))
    return ''.join(ret)

print equivalent(A = "parker", B = "morris", S = "parser") == 'makkek'
print equivalent(A = "hello", B = "world", S = "hold") == "hdld"
print equivalent(A = "leetcode", B = "programs", S = "sourcecode") == "aauaaaaada"
