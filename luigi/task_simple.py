import luigi
from luigi.mock import MockFile

class TaskMaster(luigi.Task):
    """
    This simple task prints Hello World!
    """
    def requires(self):
        """
        Which other Tasks need to be complete before
        this Task can start?
        """
        pass

    def output(self):
        return MockFile("SimpleTask", mirror_on_stderr=True)

    def run(self):
        # read through the table, and print one by one, not execute here.
        # update status after execution.
        print("James Bai:")
        _out = self.output().open('w')
        _out.write("222\n")
        _out.close()

if __name__ == '__main__':
    luigi.run(["--local-scheduler"], main_task_cls=TaskMaster)

