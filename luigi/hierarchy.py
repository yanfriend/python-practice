import luigi
 
class ATask(luigi.Task):
 
    def output(self):
        return luigi.LocalTarget("atask_output.txt")
 
    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Test")
        print "ATask was run"
 
 
class BTask(luigi.Task):
    parent_task = luigi.Parameter()
 
    def requires(self):
        return self.parent_task
 
    def output(self):
        return luigi.LocalTarget("btask_output.txt")
 
    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Test")
        print "BTask was run"
 
 
class CTask(luigi.Task):
    parent_task = luigi.Parameter()
 
    def requires(self):
        return self.parent_task
 
    def output(self):
        return luigi.LocalTarget("ctask_output.txt")
 
    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Test")
        print "CTask was run"
 
 
if __name__ == '__main__':
 
    # ---------------------------------
    # DEPENDENCY GRAPH DEFINITION
    # ---------------------------------
    atask = ATask()
    btask = BTask(atask)
    ctask = CTask(btask)
 
    # ---------------------------------
    # SET UP AND RUN THE WORKFLOW
    # ---------------------------------
    sch = luigi.scheduler.CentralPlannerScheduler()
    w = luigi.worker.Worker(scheduler=sch)
    w.add(ctask)
    w.run()
