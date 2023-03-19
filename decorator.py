from functools import wraps

#custom error
class type_error(Exception):
    def __init__(self, needed_type, found_type):
        self.msg = f'sould {needed_type} arg but found {found_type}'

    def __str__(self):
        return (self.msg)

#decorator
def type_check(_type):
    
    def decorator(func):
        
        @wraps(func)
        def wrapper(arg):
            if type(arg) != _type:
                raise (type_error(_type, type(arg)))

            return func(arg)

        return wrapper

    return decorator


#exmple
@type_check(int)
def times2(num):
    return num*2

print(times2(9))
times2('l')