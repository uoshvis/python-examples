# Python Metaclasses


**Metaprogramming** is the potential for a program to have knowledge of or manipulate itself.

Python supports a form of metaprogramming for classes called **metaclasses**.


## Old-style classes

```
>>> class Foo:
...     pass
...
>>> x = Foo()
>>> x.__class__
<class __main__.Foo at 0x000000000535CC48>
>>> type(x)
<type 'instance'>
```

## New-style classes

If obj is an instance of a new-style class, `type(obj)` is the same as `obj.__class__`

```
>>> class Foo:
...     pass
>>> obj = Foo()
>>> obj.__class__
<class '__main__.Foo'>
>>> type(obj)
<class '__main__.Foo'>
>>> obj.__class__ is type(obj)
True
```

## Type and class

!! In Python **everything is an object** !!

Classes are objects as well. Therefore, class must have a type.

```
>>> class Foo:
...     pass
...
>>> x = Foo()

>>> type(x)
<class '__main__.Foo'>

>>> type(Foo)
<class 'type'>
```

The type of any new-style class is type.

The type of type is type as well:

```
>>> type(type)
<class 'type'>
```

Just as an ordinary object is an instance of a class, any new-style class in Python, and thus any class in Python 3, is an instance of the type metaclass:
 
* x is an instance of class Foo.
* Foo is an instance of the type metaclass.
* type is also an instance of the type metaclass, so it is an instance of itself.


## Defining a Class Dynamically

You can also call `type()` with three arguments — `type(<name>, <bases>, <dct>)`:

- `<name>` specifies the class name. This becomes the `__name__` attribute of the class.
- `<bases>` specifies a tuple of the base classes from which the class inherits. This becomes the `__bases__` attribute of the class.
- `<dct>` specifies a namespace dictionary containing definitions for the class body. This becomes the `__dict__` attribute of the class.

Calling `type()` in this manner creates a new instance of the type metaclass. It dynamically creates a new class.

### Examples

**Two snippets are functionally equivalent**
### Example 1

```
>>> Foo = type('Foo', (), {})

>>> x = Foo()
>>> x
<__main__.Foo object at 0x04CFAD50>
```

```
>>> class Foo:
...     pass
...
>>> x = Foo()
>>> x
<__main__.Foo object at 0x0370AD50>
```

### Example 2
`<bases>` is a tuple with a single element Foo, specifying the parent class that Bar inherits from. An attribute, attr, is initially placed into the namespace dictionary
```
>>> Bar = type('Bar', (Foo,), dict(attr=100))

>>> x = Bar()
>>> x.attr
100
>>> x.__class__
<class '__main__.Bar'>
>>> x.__class__.__bases__
(<class '__main__.Foo'>,)
```

```
>>> class Bar(Foo):
...     attr = 100
...

>>> x = Bar()
>>> x.attr
100
>>> x.__class__
<class '__main__.Bar'>
>>> x.__class__.__bases__
(<class '__main__.Foo'>,)

```

### Example 3

A function is defined externally then assigned to attr_val in the namespace dictionary via the name f

```markdown
>>> def f(obj):
...     print('attr =', obj.attr)
...
>>> Foo = type(
...     'Foo',
...     (),
...     {
...         'attr': 100,
...         'attr_val': f
...     }
... )

>>> x = Foo()
>>> x.attr
100
>>> x.attr_val()
attr = 100
```

```markdown
>>> def f(obj):
...     print('attr =', obj.attr)
...
>>> class Foo:
...     attr = 100
...     attr_val = f
...

>>> x = Foo()
>>> x.attr
100
>>> x.attr_val()
attr = 100
```

## Custom Metaclasses

```markdown
>>> class Foo:
...     pass
...
>>> f = Foo()
```

The expression Foo() creates a new instance of class Foo. When the interpreter encounters Foo(), the following occurs:

* The `__call__()` method of Foo’s parent class is called.
Since Foo is a standard new-style class, its parent class is the type metaclass, so type’s `__call__()` method is invoked.

* That `__call__()` method in turn invokes the following:

    - `__new__()`
    - `__init__()`
    
 Suppose you wanted to similarly customize instantiation behavior when creating a class like Foo.
 You can’t reassign the __new__() method of the type metaclass.
 
###To customize instantiation of a class

**Custom metaclass**

Define a metaclass that derives from type:

```markdown
>>> class Meta(type):
...     def __new__(cls, name, bases, dct):
...         x = super().__new__(cls, name, bases, dct)
...         x.attr = 100
...         return x
...
```

The definition header `class Meta(type)`:

specifies that Meta derives from type. Since type is a metaclass, that makes Meta a metaclass as well.

Note that a custom `__new__()` method has been defined for Meta. It wasn’t possible to do that to the type metaclass directly.
The `__new__()` method does the following:

- Delegates via `super()` to the `__new__()` method of the parent metaclass (type) to actually create a new class
- Assigns the custom attribute attr to the class, with a value of 100
- Returns the newly created class


Define a new class Foo and specify that its metaclass is the custom metaclass Meta, rather than the standard metaclass type:

```markdown
>>> class Foo(metaclass=Meta):
...     pass
...
>>> Foo.attr
100
```

```markdown
>>> class Bar(metaclass=Meta):
...     pass
...
>>> class Qux(metaclass=Meta):
...     pass
...
>>> Bar.attr, Qux.attr
(100, 100)
```

In the same way that a class functions as a template for the creation of objects ,
a metaclass functions as a template for the creation of classes.

Metaclasses are sometimes referred to as **class factories.**

### Object Factory

```markdown
>>> class Foo:
...     def __init__(self):
...         self.attr = 100
...

>>> x = Foo()
>>> x.attr
100

>>> y = Foo()
>>> y.attr
100

>>> z = Foo()
>>> z.attr
100
```

### Class Factory

Allows customization of class instantiation.

```markdown
>>> class Meta(type):
...     def __init__(
...         cls, name, bases, dct
...     ):
...         cls.attr = 100
...
>>> class X(metaclass=Meta):
...     pass
...
>>> X.attr
100

>>> class Y(metaclass=Meta):
...     pass
...
>>> Y.attr
100

>>> class Z(metaclass=Meta):
...     pass
...
>>> Z.attr
100
```

## Effective alternatives

### Simple inheritance

```markdown
>>> class Base:
...     attr = 100
...

>>> class X(Base):
...     pass
...

>>> class Y(Base):
...     pass
...

>>> class Z(Base):
...     pass
...

>>> X.attr
100
>>> Y.attr
100
>>> Z.attr
100
```

### Class decorator

```markdown
>>> def decorator(cls):
...     class NewClass(cls):
...         attr = 100
...     return NewClass
...
>>> @decorator
... class X:
...     pass
...
>>> @decorator
... class Y:
...     pass
...
>>> @decorator
... class Z:
...     pass
...

>>> X.attr
100
>>> Y.attr
100
>>> Z.attr
100
```
## Conclusion

It is beneficial to understand metaclasses so that you understand Python classes in general.