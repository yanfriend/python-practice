import timeit

statements=["""\
try:
    b = 10/a
except ZeroDivisionError:
    pass""",
"""\
if a:
    b = 10/a""",
"b = 10/a"]

for a in (1,0):
    for s in statements:
        t = timeit.Timer(stmt=s, setup='a={}'.format(a))
        print("a = {}\n{}".format(a,s))
        print("%.6f usec/pass\n" % (1000000 * t.timeit(number=100000)/100000))

