import math


def ipToCIDR(s, amount):
    ip = map(int, s.split('.'))
    num = (ip[0] << 24) + (ip[1] << 16) + (ip[2] << 8) + ip[3]

    def process(num, last):
        tmp = [str(num >> 24), str((num >> 16) & 255), str((num >> 8) & 255), str(num & 255)]
        return '.'.join(tmp) + '/' + str(32 - int(math.log(last, 2)))

    ret = []
    while amount > 0:
        step = num & -num
        while step > amount:
            step = step >> 1
        ret.append(process(num, step))
        amount -= step
        num += step

    return ret


print ipToCIDR("255.0.0.7", 8)  # try n=9, n=10
# ['255.0.0.7/32', '255.0.0.8/30', '255.0.0.12/31', '255.0.0.14/32']
