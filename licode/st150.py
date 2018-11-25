class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st=[]
        for ele in tokens:
            if ele not in ('+','-','*','/'):
                st.append(int(ele))
            else:
                n2=st.pop()
                n1=st.pop()
                if ele=='+':st.append(n1+n2)
                elif ele=='-':st.append(n1-n2)
                elif ele=='*':st.append(n1*n2)
                elif ele=='/':st.append(n1/n2) # note: -1/122=-1
        return st[-1]

print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
