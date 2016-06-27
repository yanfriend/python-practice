# serial.py
import luigi
import time

class AA(luigi.Task):
    idd = luigi.IntParameter()

    def output(self):
        return luigi.LocalTarget(path='/tmp/master-%d.txt' % self.idd)

    def run(self):
        with self.output().open(mode='w') as fp:
            print '******* started', self.idd
            time.sleep(10)
            print '******* completed', self.idd


class BB(luigi.Task):
    def output(self):
        return luigi.LocalTarget(path='/tmp/master.txt')

    def run(self):

        with self.output().open(mode='w') as fp:
            for i in range(5):
                print '******* yielding', i
                yield AA(idd=i)
                # You will see this line appearing multiple times - corresponding to client.update_status(task.id, ...)
                print '******* YIELDED', i

            fp.write('done')

if __name__ == '__main__':
    luigi.run()
