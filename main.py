import signal
import time
from multiprocessing import Queue, Event

from dequeue import Dequeue
from enqueue import Enqueue

if __name__ == '__main__':
    queue = Queue()
    stop_flag = Event()

    enqueue_process = Enqueue(q=queue, interval=1, stop_flag=stop_flag)
    dequeue_process = Dequeue(q=queue, interval=1, stop_flag=stop_flag)

    [p.start() for p in [enqueue_process, dequeue_process]]


    def signal_handler(signal, handler):
        stop_flag.set()


    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        alive_flag = False
        if dequeue_process.is_alive():
            alive_flag = True
            break
        if alive_flag:
            time.sleep(0.1)
            continue
        break
