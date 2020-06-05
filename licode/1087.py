import itertools

def braceExpansion(S):
    groups=[[]]
    for ch in S:
        if ch=='{':
            if groups[-1]:
                groups.append([])
        elif ch.isalpha():
            groups[-1].append(ch)
        elif ch=='}':
            groups.append([])
    #
    print groups
    #
    # print list(itertools.product(['a', 'b'], ['c'], ['d', 'e'], ['f']))

    return map(''.join, itertools.product(*groups))

def braceExpansionII(expression):
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0: # if not 0, will give the string next level.
                    start = i + 1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0: # if >0, just parse and will pass str to next level.
                    groups[-1].append(braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:  # letters
                groups[-1].append([c])

        print groups

        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, itertools.product(*group)))
        return sorted(word_set)
#
# print braceExpansion("{a,b}c{d,e}f") # ["acdf","acef","bcdf","bcef"]
# print braceExpansion("abcd") # ["abcd"]
#
# # braceExpansionII contains braceExpansion
# print braceExpansionII("{a,b}c{d,e}f")
# print braceExpansionII("abcd")

# print braceExpansionII("{a,b}{c,{d,e}}")  # ["ac","ad","ae","bc","bd","be"]
print braceExpansionII("{{a,z},a{b,c},{ab,z}}")  # ["a","ab","ac","z"]
#
# print braceExpansionII("{abcd}")
