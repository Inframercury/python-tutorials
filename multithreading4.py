import threading
from threading import Semaphore, Thread

semaphore = Semaphore(1)

def f1():
    semaphore.acquire()
    print(semaphore)
    print(f"{threading.current_thread().name} acquired lock")
    print(semaphore._value)
    semaphore.release()
    print(f"{threading.current_thread().name} released lock")
    print(semaphore._value)



t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f1)

