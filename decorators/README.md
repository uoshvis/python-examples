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

[optional_args_decorator.py](optional_args_decorator.py)

**Stateful decorators:**

The decorator that can keep track of state.

[stateful_decorators.py](stateful_decorators.py)

**Classes as Decorators:**

Maintain state by using classes. Using class as a decorator.
`@my_decorator` == `func=my_decorator(func)`

If my_decorator is a class, it needs to take func as an argument in its `.__init__()` method.
Furthermore, the class instance needs to be callable so that it can stand in for the decorated function.

[stateful_class_decorators.py](stateful_class_decorators.py)


**Creating Singletons:**

A singleton is a class with only one instance (*None*, *True*, *False*).

None is a singleton that allows you to compare for *None* using the `is` keyword.

Using `is` returns *True* only for objects that are the exact same instance.

[singleton_decorators.py](singleton_decorators.py)

**Caching decorators**

Simple caching of the calculations.

You should use `@functools.lru_cache` instead of writing your own cache decorator. 

[caching_decorators.py](caching_decorators.py)


**Unit info decoratos**

Similar to registering plugins. Adds unit as a function attribute.

[unit_info_decorators.py](unit_info_decorators.py)

Note that you could have achieved something similar using function annotations:

```
import math

def volume(radius, height) -> "cm^3":
    return math.pi * radius**2 * height
```

However, since annotations are used for type hints,
it would be hard to combine such units as annotations with static type checking.

**Validating JSON**

```
@app.route("/grade", methods=["POST"])
def update_grade():
    json_data = request.get_json()
    if "student_id" not in json_data:
        abort(400)
    # Update database
    return "success!"
```

Let’s keep it DRY and abstract out any unnecessary logic with a decorator.
The following  `@validate_json` decorator will do the job:

```
from flask import Flask, request, abort
import functools
app = Flask(__name__)

def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json
```

1. The list of keys that must be present in the JSON is given as arguments to the decorator.
2. The wrapper function validates that each expected key is present in the JSON data.

```
@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"
```

# Conclusion

To define a decorator, you typically define a function returning a wrapper function.
The wrapper function uses *args and **kwargs to pass on arguments to the decorated function.
If you want your decorator to also take arguments, you need to nest the wrapper function inside another function.
In this case, you usually end up with three return statements.