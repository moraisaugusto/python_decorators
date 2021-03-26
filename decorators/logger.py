"""
This will handle except using a decorator and create a log file for all exceptions

log output example:
ERROR:root:exception in custom_function
=====
Traceback (most recent call last):
  File "logger.py", line 11, in wrapper
    return func(*args, **kwargs)
  File "logger.py", line 21, in custom_function
    1/0
ZeroDivisionError: division by zero
"""

from functools import wraps
import logging as logger

logger.basicConfig(filename='logger.log',  level=logger.DEBUG)

def exception(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                msg = f"Exception in {func.__name__}():\n"
                logger.exception(msg)
                raise Exception
        return wrapper
    return decorator

@exception(logger)
def custom_function():
    return 1/0

if __name__ == '__main__':
    custom_function()
