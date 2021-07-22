# Namedtuples

* `collection.namedtuple` is a memory-efficient shortcut to defining an immutable class in Python manually.

* Namedtuples can help clean up your code by enforcing an easier to understand structure on your data.

* Namedtuples provide a few useful helper methods that all start with an `_` underscore—but are part of the public interface.

**creation**
```markdown
from collections import namedtuple
Car = namedtuple('Car' , 'color mileage')

# is shorthand for:
'color mileage'.split()

Car = namedtuple('Car', ['color', 'mileage'])
my_car = Car('red', 3812.4)
my_car.color # 'red'

```
**unpacking**
```markdown
>>> color, mileage = my_car
>>> print(color, mileage)
red 3812.4
>>> print(*my_car)
red 3812.4
```

**indexing**

```markdown
>>> my_car[0]
'red'
>>> tuple(my_car)
('red', 3812.4)
```

## Subclassing Namedtuples

```markdown
>>> Car = namedtuple('Car', 'color mileage')
>>> class MyCarWithMethods(Car):
...     def hexcolor(self):
...         if self.color == 'red':
...            return '#ff0000'
...         else:
...             return '#000000'
>>> c = MyCarWithMethods('red', 1234)
>>> c.hexcolor()
'#ff0000'
```

to create hierarchies of namedtuples is to use the base tuple’s ._fields property:

```markdown
>>> Car = namedtuple('Car', 'color mileage')
>>> ElectricCar = namedtuple(
...     'ElectricCar', Car._fields + ('charge',))
```

```markdown
>>> ElectricCar('red', 1234, 45.0)
ElectricCar(color='red', mileage=1234, charge=45.0)
```

## Built-in Helper Methods

```markdown
>>> my_car._asdict()
OrderedDict([('color', 'red'), ('mileage', 3812.4)])
>>> json.dumps(my_car._asdict())
'{"color": "red", "mileage": 3812.4}'
```

shallow copy

```markdown
>>> my_car._replace(color='blue')
Car(color='blue', mileage=3812.4)
```

to create new instances of a namedtuple from a sequence or iterable:

```markdown
>>> Car._make(['red', 999])
Car(color='red', mileage=999)
```
