class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_sign='+'
        st=[]
        num=0

        s=s.replace(' ','')
        i=0
        while i<len(s):
            ch=s[i]
            if ch.isdigit():
                while i<len(s) and s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
            while i<len(s) and s[i]==' ': i+=1

            import ipdb; ipdb.set_trace()

            # not digit, not blank. +-*/ or ==len
            if pre_sign=='+':
                st.append(num)
            elif pre_sign=='-':
                st.append(-num)
            elif pre_sign=='*':
                st.append(st.pop()*num)
            elif pre_sign=='/':
                st.append(st.pop()/num)
            num=0
            if i<len(s):
                pre_sign=s[i]
                i+=1
        return sum(st)

print Solution().calculate(" 3+5 / 2 ")

