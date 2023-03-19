
import time

def timer(func, *args, ** kargs):
     tic = time.perf_counter()
     func(*args, **kargs)
     toc = time.perf_counter()
     print(f"{toc - tic:0.9f}")


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")