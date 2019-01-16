

def flat_list(lists):
    ret=[]
    for li in lists:
        if type(li)==int:
            ret.append(li)
        else:
            ret.extend(flat_list(li))
    return ret

print flat_list([0,1,[2,[3,4]],5])

# i like these codes