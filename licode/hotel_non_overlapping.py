max_profit = 0
ans = []


def max_non_overlapping(bookings):
    bookings.sort(key=lambda x: x[1])

    def helper(path, ind, profit):
        global max_profit, ans
        if ind >= len(bookings):
            if profit > max_profit:
                max_profit = profit
                ans = list(path)
                return
        for i in range(ind, len(bookings)):
            if len(path) == 0 or path[-1][1] <= bookings[i][0]:  # empty or not overlapping
                helper(path + [bookings[i][:2]], i + 1, profit + bookings[i][2])  # select this one
            else:
                helper(path, i + 1, profit)

    helper([], 0, 0)
    return ans


def max_non_overlapping_dp(bookings):
    bookings.sort(key=lambda x: x[1])
    dp = [bookings[i][2] for i in range(len(bookings))]
    parent = [i for i in range(len(bookings))]

    for i in range(1, len(bookings)):
        for j in range(i - 1, -1, -1):
            if bookings[j][1] > bookings[i][0]: continue
            if dp[j] + bookings[i][2] > dp[i]:
                dp[i] = dp[j] + bookings[i][2]
                parent[i] = j

    ind = dp.index(max(dp))
    path = [bookings[ind][:2]]
    while parent[ind] != ind:
        path.append(bookings[parent[ind]][:2])
        ind = parent[ind]
    return path[::-1]


print max_non_overlapping_dp([[2, 4, 100], [4, 8, 200], [5, 7, 300], [6, 10, 100]])
print max_non_overlapping_dp([[2, 4, 100], [5, 7, 300], [4, 8, 200]])

# can change to dp, n square time complexity
