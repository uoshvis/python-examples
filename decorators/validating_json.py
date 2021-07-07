import functools


# only difference is that we are using cls instead of func as the parameter name
# to indicate that it is meant to be a class decorator.
def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


def main():
    first_one = TheOne()
    another_one = TheOne()

    print(id(first_one))

    print(id(another_one))

    print(first_one is another_one)


if __name__ == '__main__':
    main()
