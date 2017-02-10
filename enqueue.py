# coding:utf-8
import random
import signal
import time
from multiprocessing import Queue, Process


class Enqueue(object):
    # def __init__(self, q: Queue, interval: int):
        # self.q = q
        # self.interval = interval

    # def run(self, stop_flag):
    def run(self, q: Queue, stop_flag):

        """ Signal disable
        """
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)

        while True:
            if stop_flag.is_set():
                break

            color = random.choice(["red", "blue", "green"])

            q.put(color)

            time.sleep(1)

        print("stop enqueuing!!")
