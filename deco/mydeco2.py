def d(fp):
    def _d(*args, **kwargs):
        print "Arguments were: {}, {}".format(args, kwargs)
        print "do sth before fp.."
        ret = fp(*args, **kwargs)
        print "do sth after fp.."
        return ret;
    return _d

@d
def f(i):
    print "in f() with {}".format(i)

f(2)
f([2, 3])

"""
~/repos/python-practice/deco(master) python mydeco2.py
Arguments were: (2,), {}
do sth before fp..
in f() with 2
do sth after fp..
Arguments were: ([2, 3],), {}
do sth before fp..
in f() with [2, 3]
do sth after fp..
"""
