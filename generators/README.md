# Generators intro

## Speed and memory
Lists is larger than the generator object

```
>>> import sys
>>> nums_squared_lc = [i * 2 for i in range(10000)]
>>> sys.getsizeof(nums_squared_lc)
87624
>>> nums_squared_gc = (i ** 2 for i in range(10000))
>>> print(sys.getsizeof(nums_squared_gc))
120
```

If the list is smaller than the running machine’s available memory,
then list comprehensions can be **faster** to evaluate than the equivalent generator expression.
```
>>> import cProfile
>>> cProfile.run('sum([i * 2 for i in range(10000)])')
>>> cProfile.run('sum((i * 2 for i in range(10000)))')
```
If **speed** is an issue and memory isn’t, then a **list comprehension** is likely a better tool for the job.

## Using `yield`

When the Python `yield` statement is hit, the program suspends function execution and returns the yielded value to the caller.
The state of the function is saved. This includes any variable bindings local to the generator,
the instruction pointer, the internal stack, and any exception handling.
This allows you to resume function execution whenever you call one of the generator’s methods.


In contrast, `return` stops function execution completely.

**Multiple yield**
```
>>> def multi_yield():
...     yield_str = "This will print the first string"
...     yield yield_str
...     yield_str = "This will print the second string"
...     yield yield_str
...
>>> multi_obj = multi_yield()
>>> print(next(multi_obj))
This will print the first string
>>> print(next(multi_obj))
This will print the second string
>>> print(next(multi_obj))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## Generator Methods
### using `.send()`

`yield` is an expression, rather than a statement.

 Coroutine, or a generator function into which you can pass data:
[send_example.py](send_example.py)

### using `.throw()`

.throw() allows you to throw exceptions with the generator.

```
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
```
output:
```
11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 47, in <module>
    main()
  File "advanced_gen.py", line 41, in main
    pal_gen.throw(ValueError("We don't like large palindromes"))
  File "advanced_gen.py", line 26, in infinite_palindromes
    i = (yield num)
ValueError: We don't like large palindromes
```

### using `.close()`

.close() allows you to stop a generator.

```
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
```
output:
```
11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 46, in <module>
    main()
  File "advanced_gen.py", line 42, in main
    pal_gen.send(10 ** (digits))
StopIteration
```
Raises `StopIteration`, an exception used to signal the end of a finite iterator.


### Creating Data Pipelines with Generators

You aren’t iterating through anything until you actually use a `for` loop or a function that works on iterables, like `sum()`.

[data_pipeline.py](data_pipeline.py)

