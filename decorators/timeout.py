import sys
import signal
import functools

class TimeoutError(Exception):
    def __init__(self, message=None):
        self.message = message if message else ""
        self.err = f"Details: {self.message}"
    def __str__(self):
        return str(self.message)


def timeout(seconds, error_message = "Function call timed out"):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated

import time

@timeout(1)
def slow_function():
    try:
        time.sleep(5)
    except TimeoutError as e:
        print(e)

slow_function()

