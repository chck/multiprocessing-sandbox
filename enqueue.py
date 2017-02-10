# coding:utf-8
import random
import signal
import time
from multiprocessing import Queue, Process


class Enqueue(Process):
    def __init__(self, q: Queue, interval: int, stop_flag):
        super().__init__()
        self.q = q
        self.interval = interval
        self.stop_flag = stop_flag

    def run(self):
        """ Signal disable
        """
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)

        while True:
            if self.stop_flag.is_set():
                break

            color = random.choice(["red", "blue", "green"])

            self.q.put(color)

            time.sleep(self.interval)

        print("stop enqueuing!!")
