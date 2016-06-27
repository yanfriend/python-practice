import random as rnd
import time

import luigi


class MyConfig(luigi.Task):
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
        import ipdb; ipdb.set_trace() # in config

        time.sleep(5)
        rnd.seed(self.seed)

        result = ','.join(
            [str(x) for x in rnd.sample(list(range(300)), rnd.randint(7, 25))])

        raise Exception()

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
        import ipdb; ipdb.set_trace() # in data
        print 'in Data'
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
        import ipdb; ipdb.set_trace()  # in dynamic

        try:
            # This could be done using regular requires method
            config = self.clone(MyConfig)
            aa = yield config
        except Exception as err:
            import ipdb;ipdb.set_trace()
            print 'in catching exception, will continue'

        with config.output().open() as f:
            data = [int(x) for x in f.read().split(',')]

        # ... but not this
        data_dependent_deps = [Data(magic_number=x) for x in data]
        yield data_dependent_deps

        with self.output().open('w') as f:
            f.write('Tada!')

class Dummy(luigi.Task):
    pass


class Master_Task(luigi.Task):
    def run(self):
        luigi.run(main_task_cls=Dynamic)
        # import ipdb; ipdb.set_trace()
        # print 'resume'
        # luigi.run(main_task_cls=Dummy)

        """
        yield Dynamic()
        import ipdb; ipdb.set_trace()
        print 'resuem'
        yield Dummy()
        """


#@MyConfig.event_handler(luigi.Event.FAILURE)
#def fail_action(task, exception):
#    print 'in failure handler'


if __name__ == '__main__':

    luigi.run(main_task_cls=Dynamic)

    # yield Dynamic()

    luigi.run(main_task_cls=Dynamic)
    import ipdb; ipdb.set_trace(), # luigi.run can resuem
    print 'resume ? '
    # luigi.run(main_task_cls=Data,cmdline_args=['--magic-number=8'])


# python dynamic_2.py Dynamic  --scheduler-port 10000
# luigid --port 10000luigid --port 10000

