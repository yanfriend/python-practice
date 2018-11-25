class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        i=0
        coff=0; total=0
        sign=1

        for j in range(len(equation)):

            import ipdb;ipdb.set_trace()

            if equation[j]=='+' or equation[j]=='-':
                if i<=j-1:
                    total+=sign*int(equation[i:j])
                    i=j # keep + or -, to change to int
                # change sign?
            elif equation[j]=='x': # coff operation
                if i==j or equation[j-1]=='+':
                    coff += sign
                elif equation[j-1]=='-':
                    coff -= sign
                else:
                    coff += sign*int(equation[i:j])
                i=j+1
            elif equation[j]=='=':
                if i<j: total += sign*int(equation[i:j])
                sign=-sign
                i=j+1

        if i<len(equation):
            total+=sign*int(equation[i:])

        if coff==0 and total==0: return 'Infinite solutions'
        if coff==0 and total!=0: return 'No solution'
        ret=-total/coff # move to other side of =
        return 'x={}'.format(ret)

print Solution().solveEquation("x+5-3+x=6+x-2")
