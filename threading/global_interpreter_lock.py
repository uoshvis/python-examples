# https://medium.com/python-features/pythons-gil-a-hurdle-to-multithreaded-program-d04ad9c1a63
from time import time
from threading import Thread


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def main_threaded():
    numbers = [8402868, 2295738, 5938342, 7925426]
    start = time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)
    # wait for all thread to finish
    for thread in threads:
        thread.join()
    end = time()
    print('Threaded version Took %.3f seconds' % (end - start))


def main_simple():
    numbers = [8402868, 2295738, 5938342, 7925426]
    start = time()
    for number in numbers:
        list(factorize(number))
    end = time()
    print('Main simple Took %.3f seconds' % (end - start))


if __name__ == '__main__':
    main_simple()
    main_threaded()
    # Compare times. Main_thread took more time.


