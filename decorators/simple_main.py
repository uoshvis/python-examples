from decorators import timer, debug, slow_down, register
import math
import random
from decorators import PLUGINS

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000)])


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# Registering plugins

@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)



def main():
    # example_1
    # waste_some_time(999)

    # example_2
    # make_greeting("Benjamin")
    # make_greeting("Richard", age=112)
    # make_greeting(name="Dorrisile", age=116)

    # example_3
    # prox_e = approximate_e(5)
    # print(prox_e)

    # example_4
    # countdown(3)

    # example_5 registering plugins
    print(PLUGINS)
    print(randomly_greet("Alice"))
    print(globals())


if __name__ == '__main__':
    main()



