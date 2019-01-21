def max_interval_values(intervals):
    intervals.sort(key=lambda x:x[1])

    dp=[0]*len(intervals)
    dp[0]=intervals[0][2]

    path = [[]] * len(intervals)
    path[0] = [intervals[0]]

    for i in range(1, len(intervals)):
        dp[i]=dp[i-1]
        path[i]=path[i-1]

        for j in range(i-1,-1,-1):
            if intervals[j][1]>intervals[i][0]: # overlap
                continue
            if dp[i]<=dp[j]+intervals[i][2]:
                dp[i]=dp[j]+intervals[i][2]
                path[i]=path[j]+[intervals[i]]
                break
    print path[-1]
    return dp[-1]


print max_interval_values([[2, 4, 100], [4, 8, 200], [5, 7, 300], [1,2,300],[2,5,100], [3,30,100]])

# dp to dp_path. dont use parent list to trace back
