from abc import ABCMeta, abstractmethod, abstractproperty
class Base(object):
    __metaclass__ = ABCMeta
    def __init__(self, strDirConfig):
        self.strDirConfig = strDirConfig

    @abstractmethod
    def _doStuff(self, signals):
        pass

    @abstractproperty
    def name(self):
        #this property will be supplied by the inheriting classes
        #individually
        pass


class Base_1(Base):
    __metaclass__ = ABCMeta
    # this class does not provide the name property, should raise an error
    def __init__(self, strDirConfig):
        super(Base_1, self).__init__(strDirConfig)

    def _doStuff(self, signals):
        print 'Base_1 does stuff'


class C(Base_1):
    @property
    def name(self):
        return 'class C'


if __name__ == '__main__':
    b1 = Base_1('abc')  
