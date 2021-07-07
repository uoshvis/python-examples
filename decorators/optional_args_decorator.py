import functools
import time


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def say_whee():
    print("Whee!")


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


# Slow down example

def slow_down(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


@slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


def main():
    say_whee()

    greet("Penny")

    countdown(3)


if __name__ == '__main__':
    main()


# Recipe 9.6 of the excellent Python Cookbook shows an alternative solution using functools.partial().
