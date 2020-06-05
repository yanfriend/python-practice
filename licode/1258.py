import collections
import time

def generateSentences(synonyms, text):
    '''
    synonyms: List[List[str]], text: str
    rtype: List[str]
    '''
    graph=collections.defaultdict(list)
    for s in synonyms:
        graph[s[0]].append(s[1])
        graph[s[1]].append(s[0])
    groups = []
    visited = set()

    def dfs(node): # return set
        visited.add(node)
        ret=[node]
        for child in graph[node]:
            if child not in visited:
                ret+=dfs(child)
        return ret

    for e in graph:
        for node in graph[e]:
            if node in visited: continue
            groups.append(set(dfs(node)))

    word_group=collections.defaultdict(list)
    for g in groups:
        for w in g:
            word_group[w]=sorted(list(g))

    textlst=text.split(' ')
    ret = []

    def switch(ind, path):
        if ind>=len(textlst): ret.append(' '.join(path)); return
        if textlst[ind] in word_group:
            for i in word_group[textlst[ind]]:
                switch(ind+1, path+[i])
        else: switch(ind+1, path+[textlst[ind]])

    switch(0,[])
    return ret

# -----------------------
def generateSentences2(synonyms, text):
        parent = collections.defaultdict(str)
        data = collections.defaultdict(list)

        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for p, q in synonyms:
            x, y = find(p), find(q)
            if x != y:
                parent[x] = y
        for k in parent:
            data[find(k)].append(k)

        print data

        res, texList = set(), text.split(" ")

        def dfs(index, path):
            res.add(" ".join(path))
            for i in range(index, len(texList)):
                for t in data[find(texList[i])]:
                    cur = path[:]
                    cur[i] = t
                    dfs(i + 1, cur) # many dups
                    dfs(i + 1, path)

        dfs(0, texList)
        return sorted(list(res))


start_time = time.time()
print generateSentences2(synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],text = "I am happy today but was sad yesterday")
print("--- %s mili seconds ---" % ((time.time() - start_time)*1000))

# print generateSentences2(synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],text = "I am happy today but was sad yesterday")


'''
Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
'''
