class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[]
        sign=1
        result=0
        num=0

        i=0
        while i<len(s):
            ch=s[i]

            import ipdb; ipdb.set_trace()

            if ch.isdigit():
                while i<len(s) and s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                continue # needed as i moved
            elif ch=='+':
                result+=sign*num
                num=0
                sign=1
            elif ch=='-':
                result+=sign*num
                num=0
                sign=-1
            elif ch=='(':
                st.append(result)
                st.append(sign)
                result=0; sign=1
            elif ch==')':
                result+=sign*num
                sign=st.pop()
                result=st.pop()+sign*result
                num=0; sign=1
            i+=1
        result+=sign*num # handle the last num; if have been handled, num is 0, does not matter
        return result

print Solution().calculate('1-(5)')

