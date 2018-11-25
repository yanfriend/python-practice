def getModifiedArray(length, updates):
    arr = [0] * length
    for u in updates:
        begin = u[0]
        end = u[1]
        val = u[2]
        arr[begin] += val
        if end < length - 1:
            arr[end + 1] -= val

    for i in range(1, len(arr)):
        if i > 0:
            arr[i] += arr[i - 1]
    return arr


print getModifiedArray(5, [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
])
