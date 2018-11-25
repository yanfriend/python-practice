import luigi
from luigi.task_register import Register
from six import with_metaclass

from luigi import six


class MA(type):
    def __init__(cls, name, bases, clsdict):
        if 'run' in clsdict:
            def new_run(self):
                print('before')
                clsdict['run'](self)
                print('after')
            setattr(cls, 'run', new_run)
  
class StubA(object):
    __metaclass__=MA

# B is luigi.Task, 
# MB is Register

# class AfmStub(StubA, luigi.Task):
#  pass


@six.add_metaclass(MA)
class AfmTask(luigi.Task):
# class AfmTask(with_metaclass(AfmStub, MetaTask, luigi.Task)):
    # __metaclass__=AfmStub
    pass

class SubTask(AfmTask):
    def run(self):
        print 'in subTask'

# SubTask().run()

luigi.run()
