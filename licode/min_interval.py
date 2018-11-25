# Given a list of intervals A and one interval B, find the least
# number of intervals from A that can fully cover B.
#
# If cannot find any result, just return 0;. 1point3acres.com/bbs
#
# For example:
# Given A=[[0,3],[3,4],[4,6],[2,7]] B=[0,6] return 2 since we can use [0,3] [2,7] to cover the B
# Given A=[[0,3],[4,7]] B=[0,6] return 0 since we cannot find any interval combination from A to cover the B


def findMinIntervals(intervals, target):
    """
    :type intervals: List[[int, int]]
    :type target: list[int, int]
    :rtype: int
    """
    intervals.sort()
    ret = 0
    cur_target = target[0]
    i = 0
    next_target = 0

    while i < len(intervals) and cur_target < target[1]:
        if intervals[i][0] > cur_target:
            return 0

        while i < len(intervals) and intervals[i][0] <= cur_target:
            next_target = max(next_target, intervals[i][1])
            i += 1
        cur_target = next_target
        ret += 1
    return ret if cur_target >= target[1] else 0


test = [[1,3],[2,4],[3,5],[4,7],[4,9],[7,12]]
target = [2,9]
print(findMinIntervals(test, target), 'should be 2')

test = [[1,3],[5,8],[9,12]]
target = [1,12]
print(findMinIntervals(test, target), 'should be 0')

test = [[1,3],[5,8],[2,13],[9,12]]
target = [1,12]
print(findMinIntervals(test, target), 'should be 2')

test = [[1,13]]
target = [1,12]
print(findMinIntervals(test, target), 'should be 1')

test = [[2,13]]
target = [1,12]
print(findMinIntervals(test, target), 'should be 0')

test = [[1,3],[3,8],[7,12],[2,13]]
target = [1,12]
print(findMinIntervals(test, target), 'should be 2')
