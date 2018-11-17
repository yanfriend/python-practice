class Solution(object):
    # def evaluate(self, expression):
    #     """
    #     :type expression: str
    #     :rtype: int
    #     """
    def evaluate(self, expression):
        def get_val(d, t):
            if t:
                return int(d.get(t, t))
            else:
                return 0

        def evaluate(token, d):
            t = token[0]
            if t == 'add':
                return get_val(d, token[1]) + get_val(d, token[2])
            elif t == 'mult':
                return get_val(d, token[1]) * get_val(d, token[2])
            elif t == 'let':
                for i in range(1, len(token) - 1, 2):
                    if token[i+1]:
                        d[token[i]] = get_val(d, token[i + 1])
                return get_val(d, token[-1])

        token = [''];
        d = {}
        st = []
        for c in expression:
            if c == '(':
                if token[0] == 'let':
                    evaluate(token, d)
                st.append((token, dict(d)))  # a copy of d
                token = ['']
            elif c == ')':
                num = evaluate(token, d)
                token, d = st.pop()
                token[-1] += str(num)
            elif c == ' ':
                token.append("")
            else:
                token[-1] += c
        return int(token[0])


print Solution().evaluate("(let x 1 y 2 x (add x y) (add x y))")
