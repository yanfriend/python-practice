import luigi
import random

__all__ = ['DynamicRequirements', 'SuperDynamicRequirements']

#
# Simple Dynamic. TaskWithDynamicRequirements will yield a couple of Tasks.
#
class SomeTask(luigi.Task):
    """
    Just print some number.
    """
    number = luigi.IntParameter()

    def run(self):
        with self.output().open('w') as output:
            output.write('%s\n' % self.number)

    def output(self):
        return luigi.LocalTarget('./number-%s.txt' % self.number)


class DynamicRequirements(luigi.Task):
    """
    This task has a variable number of requirements, based on a parameter.
    The required task itself depends on another parameter.
    """
    a = luigi.IntParameter(default=3)
    b = luigi.IntParameter(default=5)

    def requires(self):
        return [SomeTask(number=self.a) for i in range(self.b)]

    def run(self):
        total = 0
        for target in self.input():
            with target.open() as handle:
                total += int(handle.read().strip())
        print("%s x %s = %s" % (self.a, self.b, total))

    def complete(self):
        return False

#
# Example for a more dynamic case. RandomNumber just generates a random number,
# but SuperDynamicRequirements will need to run RandomNumber within its requires
# method to get a parameter.
#
class RandomNumber(luigi.Task):
    """
    Generate a random number.
    """
    def run(self):
        with self.output().open('w') as output:
            output.write('%s\n' % random.randint(1, 10))

    def output(self):
        return luigi.LocalTarget('./random.txt')


class SuperDynamicRequirements(luigi.Task):
    """
    This task need to run another task to find out what it requirements are.
    """
    a = luigi.IntParameter(default=3)

    def requires(self):
        prerequisite = RandomNumber()
        luigi.build([prerequisite], local_scheduler=True)
        n = int(prerequisite.output().open().read().strip())
        return [SomeTask(number=self.a) for i in range(n)]
        
    def run(self):
        total = 0
        for target in self.input():
            with target.open() as handle:
                total += int(handle.read().strip())
        print("%s x %s = %s" % (self.a, len(self.input()), total))

    def complete(self):
        return False


if __name__ == '__main__':
    luigi.run()
