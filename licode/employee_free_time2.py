def employee_free_time2(employee_times):
    flatten_times = []
    for e in employee_times:
        flatten_times += e

    flatten_times.sort(key=lambda x: x[0])

    ret = []
    tmp = flatten_times[0]
    for itv in flatten_times[1:]:
        if tmp[1] < itv[0]:
            ret.append([tmp[1], itv[0]])
        tmp[1] = max(tmp[1], itv[1])
    return ret


print employee_free_time2([
    [[1, 3], [6, 7]],
    [[2, 4]],
    [[2, 3], [9, 12]]
])
# [[4, 6], [7, 9]]
