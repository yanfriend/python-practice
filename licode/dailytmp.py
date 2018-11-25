class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(T)
        st=[]
        for i in range(len(T)-1,-1,-1):
            while st and T[st[-1]]<=T[i]:
                st.pop()
            ans[i]=st[-1]-i if st else 0
            st.append(i)
        return ans

print Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
