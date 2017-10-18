import time
import threading


class LimitThread(object):
    def __init__(self):
        self.thread_num=0

    def func(self):
        print 'a'
        time.sleep(10)

    def run_one(self):
        # lock,
        if self.thread_num>2: return
        tmp=threading.Thread(target=self.func)
        self.thread_list.append(tmp)

        tmp.start()
        tmp.join()


for i in range(3):
    LimitThread().run_one()

