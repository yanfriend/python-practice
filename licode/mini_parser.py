def mini_parser(s):
    if s is None or s == '': return 'E'

    if s[0] != '[':  # only int
        return int(s)

    ret = []

    # for case of '[xxx]'
    if len(s)==2: return ret # empty '[]'

    start = 1
    cnt = 0
    for i in range(1, len(s)):
        char = s[i]
        if cnt == 0 and (char == ',' or i == len(s) - 1):  # last is ']'
            ret.append(mini_parser(s[start:i]))
            start = i + 1
        elif char == '[':
            cnt += 1
        elif char == ']':
            cnt -= 1
    return ret


print mini_parser('234')
print mini_parser('[123,[456,[789]]]')
