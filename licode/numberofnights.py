def number_nights(living_night):
    p_2 = 0
    p_1 = living_night[0]

    for n in living_night[1:]:
        tmp = max(p_2 + n, p_1)
        p_2, p_1 = p_1, tmp
    return max(p_1, p_2)


print number_nights([6, 5, 0, 1, 0, 9])  # 16
print number_nights([5, 6, 3, 1])  # 8
print number_nights([5, 1, 1, 5])  # 10
print number_nights([3, 6, 4])  # 7
print number_nights([4, 10, 3, 1, 5])  # 15

assert number_nights([4, 10, 3, 1, 5]) == 15
