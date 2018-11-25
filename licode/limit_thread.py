import urllib2
from multiprocessing.dummy import Pool as ThreadPool

import time

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  # etc..
  ]

# # Make the Pool of workers
# pool = ThreadPool(4)
# # Open the urls in their own threads
# # and return the results
# results = pool.map(urllib2.urlopen, urls)
# #close the pool and wait for the work to finish
# pool.close()
# pool.join()
#
# print results


results = []

bt=time.time()

for url in urls:
  result = urllib2.urlopen(url)
  results.append(result)

et=time.time()
print et-bt

# # ------- VERSUS ------- #

bt=time.time()
# # ------- 4 Pool ------- #
pool = ThreadPool(2)
results = pool.map(urllib2.urlopen, urls)
et=time.time()
print et-bt


# # ------- 8 Pool ------- #

bt=time.time()

pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)

et=time.time()
print et-bt


#
# # # ------- 13 Pool ------- #
# bt=time.time()
#
# pool = ThreadPool(13)
# results = pool.map(urllib2.urlopen, urls)
#
# et=time.time()
# print et-bt


#
# import threading
# import time
#
#
# from Queue import Queue
# from threading import Thread
#
#
# class Worker(Thread):
#     """ Thread executing tasks from a given tasks queue """
#     def __init__(self, tasks):
#         Thread.__init__(self)
#         self.tasks = tasks
#         self.daemon = True
#         self.start()
#
#     def run(self):
#         while True:
#             func, args, kargs = self.tasks.get()
#             try:
#                 func(*args, **kargs)
#             except Exception as e:
#                 # An exception happened in this thread
#                 print(e)
#             finally:
#                 # Mark this task as done, whether an exception happened or not
#                 self.tasks.task_done()
#
#
# class ThreadPool:
#     """ Pool of threads consuming tasks from a queue """
#     def __init__(self, num_threads):
#         self.tasks = Queue(num_threads)
#         for _ in range(num_threads):
#             Worker(self.tasks)
#
#     def add_task(self, func, *args, **kargs):
#         """ Add a task to the queue """
#         self.tasks.put((func, args, kargs))
#
#     def map(self, func, args_list):
#         """ Add a list of tasks to the queue """
#         for args in args_list:
#             self.add_task(func, args)
#
#     def wait_completion(self):
#         """ Wait for completion of all the tasks in the queue """
#         self.tasks.join()
#
#
# if __name__ == "__main__":
#     from random import randrange
#     from time import sleep
#
#     # Function to be executed in a thread
#     def wait_delay(d):
#         print("sleeping for (%d)sec" % d)
#         sleep(d)
#
#     # Generate random delays
#     delays = [randrange(3, 7) for i in range(50)]
#
#     # Instantiate a thread pool with 5 worker threads
#     pool = ThreadPool(5)
#
#     # Add the jobs in bulk to the thread pool. Alternatively you could use
#     # `pool.add_task` to add single jobs. The code will block here, which
#     # makes it possible to cancel the thread pool with an exception when
#     # the currently running batch of workers is finished.
#     pool.map(wait_delay, delays)
#     pool.wait_completion()



#
# class LimitThread(object):
#     def __init__(self):
#         self.thread_list=[]
#
#     def func(self):
#         print 'a'
#         time.sleep(10)
#
#     def run_one(self):
#         # lock,
#         if len(self.thread_list)>2: return
#         tmp=threading.Thread(target=self.func)
#         self.thread_list.append(tmp)
#
#         tmp.start()
#         tmp.join()
#
#
# for i in range(3):
#     LimitThread().run_one()
