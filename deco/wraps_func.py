from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called"
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print f.__name__  # prints 'f'
print f.__doc__  # prints 'does some math'

print ""

print f(25)

"""
yanzhibai@MacBook-Pro.local:~/repos/python-practice/deco$ python wraps_func.py # keep @wraps
f
does some math
yanzhibai@MacBook-Pro.local:~/repos/python-practice/deco$
yanzhibai@MacBook-Pro.local:~/repos/python-practice/deco$ python wraps_func.py # comment out @wraps
with_logging
None

have @wrap is the correct one
"""
