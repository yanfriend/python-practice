def nested_list_weight(nested_list):
    def helper(nested):
        sumi = 0
        suml = 0
        max_level = 0
        for l in nested:
            if type(l) == int:
                sumi += l
            else:
                s, level = helper(l)
                suml += s
                max_level = max(max_level, level)
        max_level += 1
        return sumi * max_level + suml, max_level

    ret, level = helper(nested_list)
    return ret


print nested_list_weight([[1, 1], 2, [1, 1]])  # 2*2+4*1
print nested_list_weight([1, [4, [6]]])  # 1*3, 4*2, 6*1
