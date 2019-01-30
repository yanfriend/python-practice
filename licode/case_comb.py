def case_comb(s):
    ret = []

    def helper(ind, path):
        if ind >= len(s):
            ret.append(path)
            return
        helper(ind + 1, path + s[ind].lower())
        helper(ind + 1, path + s[ind].upper())

    helper(0, '')
    return ret


print case_comb('abc')
