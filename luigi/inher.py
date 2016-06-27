# parallel.py
import luigi
import time

from luigi.util import inherits


class AA(luigi.Task):
    idd1 = luigi.IntParameter()

    def output(self):
        return luigi.LocalTarget(path='/tmp/master-%d.txt' % self.idd)

    def run(self):
        with self.output().open(mode='w') as fp:
            print '******* started', self.idd
            time.sleep(30)
            print '******* completed', self.idd


@inherits(AA)
class BB(luigi.Task):

    # idd0 = luigi.IntParameter()

    idd2 = luigi.IntParameter()

    #def __init__(self, *args, **kwargs):
    #    super(BB, self).__init__(idd1=self.idd1, *args, **kwargs)

    def output(self):
        return luigi.LocalTarget(path='/tmp/master.txt')

    def run(self):
        with self.output().open(mode='w') as fp:
            yield [AA(idd=i) for i in range(5)]
            fp.write('done')

if __name__ == '__main__':
    luigi.run(main_task_cls=BB(idd1=1, idd2=2))
