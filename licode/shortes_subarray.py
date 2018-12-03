import collections


def shortestSubarray(A, K):
    N = len(A)
    B = [0] * (N + 1)
    for i in range(N): B[i + 1] = B[i] + A[i]
    d = collections.deque()
    res = N + 1

    for i in xrange(N + 1):
        while d and B[i] - B[d[0]] >= K: res = min(res, i - d.popleft())
        while d and B[i] <= B[d[-1]]: d.pop()
        d.append(i)
    return res if res <= N else -1


print shortestSubarray([4, -1, 2, 3], 9)

# [0,4,3,5,8] # for presum
# deque changes:
#  0   3
#      3,5
#        5,8

# why remove index 1, i.e. 4 in presum? you never start with -1.
