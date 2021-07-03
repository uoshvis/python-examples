# Decorators

Decorators wrap a function, modifying its behavior

function -- first-class object

func() -- execute func

func --- pass reference to func

@ - syntactic sugar

@my_decorator ==> say_whee=my_decorator(say_whee)

Decorator is a regular python function

###Introspection

```
>>> say_whee
<function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>

>>> say_whee.__name__
'wrapper_do_twice'

>>> help(say_whee)
Help on function wrapper_do_twice in module decorators:

wrapper_do_twice()
```
In order the introspection to work properly:

```
import functools
@functools.wraps(func)
```

The @functools.wraps decorator uses the function functools.update_wrapper() to update special attributes like __name__ and __doc__ that are used in the introspection.


#### Simple decorators examples

[simple_decorators.py](simple_decorators.py)

[simple_main.py](simple_main.py)
