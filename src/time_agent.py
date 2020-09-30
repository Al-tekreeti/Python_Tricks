from contextlib import contextmanager
import time

@contextmanager
def timeGauger():
    """ Measuring the execution time of a block of code using context manager decorator and class"""
    try:
        secs1 = time.time()
        yield 
    finally:
        secs2 = time.time()
        print(f'The execution time is {secs2 - secs1} using context manager decorator')

def getFactorial(num):
    if num == 0:
        return 1
    return num * getFactorial(num - 1)

class TimeGauger:
    def __init__(self):
        print("Initializing...")
    def __enter__(self):
        self._seconds = time.time()
        print("Entering...")
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'The execution time is {time.time() - self._seconds} using context manager class')


if __name__ == '__main__':
    num = 5
    with timeGauger():
        fact = getFactorial(num)

    print(f'Factorial of {num} is {fact}')

    num = 5
    with TimeGauger() as t:
        fact = getFactorial(num)
    
    print(f'Factorial of {num} is {fact}')


