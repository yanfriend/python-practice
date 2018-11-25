class B(object):
    def __init__(self):
        print 'B.__init__'; # super(B,self).__init__()

class C(object):
    def __init__(self):
        print 'C.__init__'; # super(C,self).__init__()

class D(B,C):
    pass

x=B()
y=C()

z=D()

"""
output
~/repos/python-practice/my_super(master) python inhe.py
B.__init__
C.__init__
B.__init__
"""

class B(object):
    def __init__(self):
        print 'B.__init__'; super(B,self).__init__()

class C(object):
    def __init__(self):
        print 'C.__init__'; super(C,self).__init__()

class D(B,C):
    pass

x=B()
y=C()

z=D()

"""output
B.__init__
C.__init__

B.__init__
C.__init__
"""


"""
if without super, subclass only calls the leftmost edge.
with super class calls super, it call all, and avoid diomand issue too, and super class init is called only once.
(not in this example)
"""
