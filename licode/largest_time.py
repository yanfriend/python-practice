ans = ''


class Solution(object):

    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """


        def perm(ind, path):
            global ans
            if ind == 4:
                hour = int(path[:2])
                minute = int(path[2:])
                if hour < 24 and minute < 60 and path > ans:
                    ans = path
                return
            for i in range(ind, 4):
                A[ind], A[i] = A[i], A[ind]
                perm(ind + 1, path + str(A[ind]))
                A[ind], A[i] = A[i], A[ind]

        perm(0, '')
        return ans[:2]+':'+ans[2:]


print Solution().largestTimeFromDigits([1,2,3,4])
