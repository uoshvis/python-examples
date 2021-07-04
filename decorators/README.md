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


### Simple decorators

[simple_decorators.py](decorators.py)

[simple_main.py](simple_main.py)

### Fancy decorators

#### Decorating Classes

**Built-in class decorators:**

The `@classmethod` and `@staticmethod` decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class.

The `@property` decorator is used to customize getters and setters for class attributes.

[built_in_decorators.py](built_in_decorators.py)

**Decorating class methods:**

[decorating_class_method.py](decorating_class_method.py)


**Decorate the whole class**

```
from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str
```
Equal decoration: `PlayingCard = dataclass(PlayingCard)`

A common use of class decorators is to be a simpler alternative to some use-cases of metaclasses.
In both cases, you are changing the definition of a class dynamically.

Decorating a class does not decorate its methods.
Recall that @timer is just shorthand for TimeWaster = timer(TimeWaster).

[decorating_class.py](decorating_class.py)

**Nesting decorators**
You can apply several decorators to a function by stacking them on top of each other.

[nesting_decorators.py](nesting_decorators.py)

**Decorators with arguments:**

[argument_decorators.py](argument_decorators.py)

**Decorators with and without arguments:**


