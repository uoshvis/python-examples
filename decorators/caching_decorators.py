import functools
from decorators import count_calls


def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


# @cache
# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)

# You should use @functools.lru_cache instead of writing your own cache decorator

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def main():
    print(fibonacci(8))

    print(fibonacci(10))

    print(fibonacci(8))

    print(fibonacci.cache_info())


if __name__ == '__main__':
    main()
