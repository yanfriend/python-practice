def flatten(l):
    ret=[]

    for it in l:
        if type(it)==int: # do not use 'int', int, list directly.
            ret.append(it)
        else: # list
            ret.extend(flatten(it))
    return ret

print flatten([[1,1],2,[1,1]])
print flatten([1,[4,[6]]])
