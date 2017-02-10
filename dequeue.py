# coding:utf-8
import signal
import time
from multiprocessing import Queue, Process


class Dequeue(Process):
    def __init__(self, q: Queue, interval: int, stop_flag):
        super().__init__()
        self.q = q
        self.interval = interval
        self.stop_flag = stop_flag

    def run(self):
        """Signal disable
        """
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)

        while True:
            if self.stop_flag.is_set():
                break

            if not self.q.empty():
                print("GET:::{}".format(self.q.get()))

            time.sleep(self.interval)

        print("stop enqueuing!!")
