from functools import wraps

def twice_decorator(func):
    @wraps(func)
    def function_wrapper(*args, **kargs):
        func(*args, **kargs)
        func(*args, **kargs)

    return function_wrapper

@twice_decorator
def f(i):
    print(i)

f('Hello')