# -*- coding: utf-8 -*-
import random
import time
from threading import Thread, Lock

database_value = 0

def increase(lock):
    global database_value
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == "__main__":
    threads = []
    num_threads = 10

    lock = Lock()

    print("Start value", database_value)
    for i in range(num_threads):
        thread = Thread(target=increase, args=(lock,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("End value", database_value)
    print("end main")