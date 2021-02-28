import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


def lowercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper


@lowercase
def hello_function():
    return "Hello"

