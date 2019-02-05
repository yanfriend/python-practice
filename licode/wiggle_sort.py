def wiggle_sort(numbers):
    def quick_sort(start, end, k):  # k is index
        # error 0!, lost cos not use start, end. Use index instead of cut list
        pivot = numbers[end]
        l = start
        for i in range(start, end):
            if numbers[i] < pivot:
                numbers[i], numbers[l] = numbers[l], numbers[i]  # error 1, mess up l, i
                l += 1
        numbers[l], numbers[end] = numbers[end], numbers[l]
        if l == k:
            return
        elif l < k:
            quick_sort(l + 1, end, k)
        else:
            quick_sort(start, l - 1, k)

    k = (len(numbers) + 1) / 2 - 1  # if length is 6, k=2, if 5, k=2, first half (lower) is longer
    higher = len(numbers) - 1
    lower = k

    quick_sort(0, len(numbers) - 1, k)

    ret = []
    for i in range(len(numbers)):
        if i % 2 == 1:
            ret.append(numbers[higher])  # error 2, [] but used index, should append
            higher -= 1
        else:
            ret.append(numbers[lower])
            lower -= 1
    return ret


print wiggle_sort([1, 5, 1, 1, 6, 4])
print wiggle_sort([1, 5, 1, 1, 4])
