"""
ID: baifriend
LANG: PYTHON2
PROG: ride
"""


def line_int(line):
    sm = 1
    for i in range(len(line)):
        if 'A' <= line[i] <= 'Z':
            sm *= ord(line[i]) - ord('A') + 1
    return sm % 47


fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

line1 = fin.readline()
line2 = fin.readline()

ret = ''
if line_int(line1) == line_int(line2):
    ret = 'GO'
else:
    ret = 'STAY'

fout.write(ret + '\n')
fout.close()
