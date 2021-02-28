from contextlib import contextmanager
from time import time, sleep

class SomeContextManager:
    def __enter__(self):
        print("Enter")

    def __exit__(self, *args):
        print("Exit")

@contextmanager
def timed(label):
    start = time()  # Setup - __enter__
    print(f"{label}: Start at {start}")
    try:
        yield  # yield to body of `with` statement
    finally:  # Teardown - __exit__
        end = time()
        print(f"{label}: End at {end} ({end - start} elapsed)")


with SomeContextManager() as cm:
    print("Hello")
    raise ValueError("Some error happened")