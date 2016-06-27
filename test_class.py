
class A(object):
    @classmethod
    def whole_level(cls):
        print "class"
    
    def foo(self):
        print 'Foo'
        A.whole_level()

    def bar(self, an_argument):
        print 'Bar', an_argument


if __name__ == "__main__":
    A.whole_level()
    aa = A()
    aa.foo()
