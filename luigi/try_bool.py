# parallel.py
import luigi
import time

# this is a bad example. 
# BoolParameter instead of BooleanParameter(depreciated), which default value is False
# use --foo to pass in True.

class Boo(luigi.Task):
    foo = luigi.BoolParameter(default=True)

    def output(self):
        return luigi.LocalTarget(path='/tmp/master-%d.txt' % 0)

    def run(self):
        # import ipdb; ipdb.set_trace()
        print self.foo

if __name__ == '__main__':
    luigi.run()
