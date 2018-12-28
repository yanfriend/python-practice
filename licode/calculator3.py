class Solution(object):
    def calculate(self, s):
        s = s + '='
        operands = []
        operators = []
        base = 0
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '=': float('-inf')}

        def cal(op, n2, n1):
            if op == '+':
                return n1 + n2
            elif op == '-':
                return n1 - n2
            elif op == '*':
                return n1 * n2
            elif op == '/':
                return n1 / n2
            return 0

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while s[i].isdigit(): # while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                operands.append(num)
                i -= 1
            elif s[i] == '(':
                base += 5
            elif s[i] == ')':
                base -= 5
            elif s[i] in '+-*/=':
                while operators and operators[-1][1] >= (base + precedences[s[i]]):
                    op, _ = operators.pop()
                    operands.append(cal(op, operands.pop(), operands.pop()))
                operators.append((s[i], base + precedences[s[i]]))
            i += 1
        return operands[0]




    def calculate_recursive(self, s): # this is also a good. might save some space? but recursions
        ans = 0; curr_ans = 0
        sign = 1; prev_op=-1 # 0-mul 1-div
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num=0
                while i<len(s) and s[i].isdigit():
                    num = num * 10 + int(ord(s[i]) - ord('0'))
                    i+=1
                if prev_op==0:
                    curr_ans=curr_ans*num
                elif prev_op==1:
                    curr_ans=curr_ans/num
                else: curr_ans=num
                i-=1
            elif ch == '(':
                # find corresponding )
                cnt=1
                for j in range(i+1, len(s)):
                    if s[j]=='(': cnt+=1
                    elif s[j]==')': cnt-=1
                    if cnt==0: break
                num = self.calculate(s[i+1:j])
                if prev_op==0:
                    curr_ans=curr_ans*num
                elif prev_op==1:
                    curr_ans=curr_ans/num
                else: curr_ans=num
                i=j
            elif ch in '+-*/':
                if ch in '+-':
                    ans = ans + sign * curr_ans
                    sign = 1 if ch == '+' else -1
                    prev_op=-1
                elif ch == '*':  # */
                    prev_op=0
                else:
                    prev_op=1

            i+=1
        ans+=sign*curr_ans
        return ans

print Solution().calculate('2+6')
print Solution().calculate('(2+6)')
print Solution().calculate('(2+6*3)')

print Solution().calculate("(2+6*3+5-(3*14/7+2)*5)+3")  # =-12
print Solution().calculate('3*14/7+2')
