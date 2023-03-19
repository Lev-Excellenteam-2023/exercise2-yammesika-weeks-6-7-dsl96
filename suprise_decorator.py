from functools import wraps


def suprise_decorator(func):
    @wraps(func)
    def function_wrapper(*args, **kargs):
        print( 'suprise!')
    return function_wrapper

@suprise_decorator
def f():
    for i in range(900):
        print(i)

f()