class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = 0
        st = []
        heights.append(0)
        for i in range(len(heights)):
            if len(st) == 0 or heights[i] > heights[st[-1]]:
                st.append(i)
            else:
                while len(st) > 0 and heights[st[-1]] > heights[i]:
                    h = heights[st.pop()]
                    ret = max(ret, (i - 1 - (st[-1] if len(st) > 0 else -1)) * h)
                st.append(i)
        return ret

print(Solution().largestRectangleArea([2,1,3]))

