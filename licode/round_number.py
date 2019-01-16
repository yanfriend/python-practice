from math import floor


def roundNum(input):
    output = map(lambda x: int(x), input)
    remain = int(round(sum(input)) - sum(output))
    it = sorted(enumerate(input), key=lambda x: x[1] - int(x[1]))  # (index, value)
    for _ in xrange(remain):
        output[it.pop()[0]] += 1
    return output


print roundNum([30.3, 2.4, 3.5])  # 30,2,4; +1 from the biggest diff
print roundNum([30.9, 2.4, 3.9]) # 31 2 4; sum and round 
