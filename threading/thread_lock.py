# https://medium.com/python-features/using-locks-to-prevent-data-races-in-threads-in-python-b03dfcfbadd6
import threading


# Accumulate total count of all processed items
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


#  By using a lock, we can have the Counter class protect
#  its current value against simultaneous access from multiple threads.
class LockingCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self):
        # here we use with statement to acquire and release the lock
        # this make it easier to see which code is executing while the lock is held
        with self.lock:
            self.count += 1


# Each sensors has its own worker thread for processing items
def worker(sensor_idx, items, counter):
    for _ in range(items):
        # Read from the sensor
        # ...
        # increment counter
        counter.increment()


# Starts worker for each sensor and waits for them all to finish
def run_threads(func, items, counter):
    threads = []
    for i in range(5):
        args = (i, items, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def main():
    # Running five threads in parallel
    items = 100000
    counter = Counter()
    run_threads(worker, items, counter)
    print('Counter should be {}, found {}'.format(5*items, counter.count))
    # The Lock resolves the problem.
    locked_counter = LockingCounter()
    run_threads(worker, items, locked_counter)
    print('Locked counter should be {}, found {}'.format(5*items, locked_counter.count))


if __name__ == '__main__':
    main()
