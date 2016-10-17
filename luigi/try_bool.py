# parallel.py
import luigi
import time

# this is a bad example. 
# BoolParameter instead of BooleanParameter(depreciated), which default value is False
# use --foo to pass in True.
# luigi does not support dynamic parameter as num = luigi.IntParameter(default = (0,1)[int(foo)])
class Boo(luigi.Task):
    foo = luigi.BoolParameter()
    num = luigi.IntParameter(default = (0,1)[int(foo)])

    def output(self):
        return luigi.LocalTarget(path='/tmp/master-%d.txt' % 0)

    def run(self):
        # import ipdb; ipdb.set_trace()
        print self.foo, self.num

if __name__ == '__main__':
    luigi.run()
