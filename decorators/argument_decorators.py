import functools


def repeat(num_times):  # should return a function object that can act as a decorator.
    # decorator func
    #  we reserve the base name—repeat()—for the outermost function
    def decorator_repeat(func):
        @functools.wraps(func)
        #  takes arbitrary arguments and returns the value of the decorated function, func()
        def wrapper_repeat(*args, **kwargs):
            # loop calls the decorated function num_times time
            #  num_times parameter that must be supplied from the outside
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    # outermost function returns a reference to the decorator function
    return decorator_repeat


'''
Defining decorator_repeat() as an inner function means that repeat() will refer to a function object—decorator_repeat.
Earlier, we used repeat without parentheses to refer to the function object.
The added parentheses are necessary when defining decorators that take arguments.

The num_times argument is seemingly not used in repeat() itself.
But by passing num_times a closure is created where the value of num_times is stored until
it will be used later by wrapper_repeat().
'''


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


def main():
    greet("World")


if __name__ == '__main__':
    main()
