# coding:utf-8
import signal
import time
from multiprocessing import Queue


class Dequeue(object):
    def run(self, q: Queue, stop_flag):
        """Signal disable
        """
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)

        while True:
            if stop_flag.is_set():
                break

            if not q.empty():
                print("GET:::{}".format(q.get()))

            time.sleep(1)

        print("stop enqueuing!!")
