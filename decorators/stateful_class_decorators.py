import functools


class CountCalls:
    def __init__(self, func):
        # use update_wrapper instead wraps
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # The .__call__() method is executed each time you try to call an instance of the class
    # The .__call__() method will be called instead of the decorated function.
    # It does essentially the same thing as the wrapper() function in our earlier examples.
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Call {self.num_calls} of {self.func.__name__!r}')
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print('Whee?')


def main():
    say_whee()

    say_whee()

    print(say_whee.num_calls)


if __name__ == '__main__':
    main()
