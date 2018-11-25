
val=1

def func1():
    global val
    print 'func1', val,
    val=2
    func2()


def func2():
    print 'func2', val


func1()


"""
~/repos/python-practice/licode(master ✗) python functions.py
func1 1 func2 2
"""

