import random as rnd
import time

import luigi


class Config(luigi.Task):
    seed = luigi.IntParameter()

    def output(self):
        """
        Returns the target output for this task.
        In this case, a successful execution of this task will create a file on the local filesystem.
        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """
        return luigi.LocalTarget('/tmp/Config_%d.txt' % self.seed)

    def run(self):
        time.sleep(5)
        rnd.seed(self.seed)

        result = ','.join(
            [str(x) for x in rnd.sample(list(range(300)), rnd.randint(7, 25))])
        with self.output().open('w') as f:
            f.write(result)


class Data(luigi.Task):
    magic_number = luigi.IntParameter()

    def output(self):
        """
        Returns the target output for this task.
        In this case, a successful execution of this task will create a file on the local filesystem.
        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """
        return luigi.LocalTarget('/tmp/Data_%d.txt' % self.magic_number)

    def run(self):
        time.sleep(1)
        with self.output().open('w') as f:
            f.write('%s' % self.magic_number)


class Dynamic(luigi.Task):
    seed = luigi.IntParameter(default=1)

    def output(self):
        """
        Returns the target output for this task.
        In this case, a successful execution of this task will create a file on the local filesystem.
        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """
        return luigi.LocalTarget('/tmp/Dynamic_%d.txt' % self.seed)

    def run(self):
        # This could be done using regular requires method
        config = self.clone(Config)
        yield config

        with config.output().open() as f:
            data = [int(x) for x in f.read().split(',')]

        # ... but not this
        data_dependent_deps = [Data(magic_number=x) for x in data]
        yield data_dependent_deps

        with self.output().open('w') as f:
            f.write('Tada!')


if __name__ == '__main__':
    luigi.run()
