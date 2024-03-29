import math

"""
Given a start IP address ip and a number of ips we need to cover n, 
return a representation of the range as a list (of smallest possible length) of CIDR blocks.

A CIDR block is a string consisting of an IP, followed by a slash, 
and then the prefix length. For example: "123.45.67.89/20". 
That prefix length "20" represents the number of common prefix bits in the specified range.
"""

def ipToCIDR(ip, n):
    """
    :param ip:
    :param n:
    :return: a list of ip/subnet
    """
    ips = ip.split('.')

    x = 0
    for aip in ips:
        x = (x << 8) + int(aip)
    # print x

    # x=y=(int(ips[0]))<< 24 | (int(ips[1]))<<16 | (int(ips[2])) <<8 | int(ips[3])
    # print y
    #
    # z=((int(ips[0])) << 24) + ((int(ips[1])) << 16) + ((int(ips[2])) << 8) + int(ips[3])
    # print z

    res = []

    def convert(x, step):
        return str(x >> 24 & 255) + '.' + str(x >> 16 & 255) + '.' + str(x >> 8 & 255) + '.' + str(x & 255) + \
               '/' + str(32 - int(math.log(step, 2)))

    while n > 0:
        step = x & -x  # right most 1 as only 1
        while step > n: step >>= 1
        res.append(convert(x, step))
        n -= step
        x += step

    return res


print ipToCIDR("255.0.0.7", 8) # try n=9, n=10
['255.0.0.7/32', '255.0.0.8/30', '255.0.0.12/31', '255.0.0.14/32']
