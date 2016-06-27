def d(fp):
    def _d(*args, **kwargs):
        print "Arguments were: %s, %s" % (args, kwargs)
        print "do sth before fp.."
        r = fp(*args, **kwargs)
        print "do sth after fp.."
        return r;
    return _d

@d
def f(i):
    print "in f() with %s" % i

f(2)
f([2, 3])
