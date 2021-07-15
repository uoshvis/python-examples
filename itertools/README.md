# Intro to Itertools

Technically, any Python object that implements the `.__iter__()` or `.__getitem__()` methods is iterable.

[Itertools recipes](https://docs.python.org/3.6/library/itertools.html#itertools-recipes)

### chain()
```
import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

list(itertools.chain(letters, booleans, decimals))

>>> ['a', 'b', 'c', 'd', 'e', 'f', 1, 0, 1, 0, 0, 1, 0.1, 0.7, 0.4, 0.4, 0.5]
```

### ifilter()

```
list(itertools.ifilter(lambda x: x % 2, numbers))
>>> [23, 7]
```

### count()
```
for i in itertools.count(10, 0.25):
    if i < 20:
        do_something()
    else:
        break
```

### compress()
```
print list(itertools.compress(letters, booleans))
```

### imap()
```
print list(itertools.imap(mult, numbers, decimals))

> [2.2, 14.0, 17.6, 12.8, 3.5]
```
Passing `None`
```
print list(itertools.imap(None, numbers, decimals))

> [(22, 0.1), (20, 0.7), (44, 0.4), (32, 0.4), (7, 0.5)]
```

### Unique everseen

```
def unique_everseen(utterable, key=None):
"List unique elements, preserving order. Remember all elements ever seen."
# unique_everseen('AAAABBBCCDAABBB') --> A B C D
# unique_everseen('ABBCcAD', str.lower) --> A B C D
seen = set()
seen_add = seen.add
if key is None:
    for element in ifilterfalse(seen.__contains__, utterable):
        seen_add(element)
        yield element
else:
    for element in utterable:
        k = key(element)
        if k not in seen:
            seen_add(k)
            yield element
```

### Grouper


[grouper_example.py](grouper_example.py)
```
>>> import itertools as it
>>> x = [1, 2, 3, 4, 5]
>>> y = ['a', 'b', 'c']
>>> list(zip(x, y))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> list(it.zip_longest(x, y))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]
```

### Combinations

```
>>> combinations([1, 2, 3], 2)
(1, 2), (1, 3), (2, 3)
```

```
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
list(it.combinations(bills, 3))
# [(20, 20, 20), (20, 20, 10), (20, 20, 10), ... ]
 
makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)
set(makes_100)
```

Combinations_with_replacement() allows elements to be repeated in the tuples it returns
```
>>> list(it.combinations_with_replacement([1, 2], 2))
[(1, 1), (1, 2), (2, 2)]
```
versus
```
>>> list(it.combinations([1, 2], 2))
[(1, 2)]
```

```
>>> bills = [50, 20, 10, 5, 1]
>>> make_100 = []
>>> for n in range(1, 101):
...     for combination in it.combinations_with_replacement(bills, n):
...         if sum(combination) == 100:
...             makes_100.append(combination)
```

### Permutations
```
>>> list(it.permutations(['a', 'b', 'c']))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'),
 ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```
### Sequences of numbers

Evens and odds

```markdown
>>> def evens():
...     """Generate even integers, starting with 0."""
...     n = 0
...     while True:
...         yield n
...         n += 2
...
>>> evens = evens()
>>> list(next(evens) for _ in range(5))
[0, 2, 4, 6, 8]

>>> def odds():
...     """Generate odd integers, starting with 1."""
...     n = 1
...     while True:
...         yield n
...         n += 2
...
>>> odds = odds()
>>> list(next(odds) for _ in range(5))
[1, 3, 5, 7, 9]

```

Using counter
#### count()
```markdown
>>> counter = it.count()
>>> list(next(counter) for _ in range(5))
[0, 1, 2, 3, 4]
```

```markdown
>>> evens = it.count(step=2)
>>> list(next(evens) for _ in range(5))
[0, 2, 4, 6, 8]

>>> odds = it.count(start=1, step=2)
>>> list(next(odds) for _ in range(5))
[1, 3, 5, 7, 9]
```
Enumerating without a `for` loop 

```markdown
>>> list(zip(it.count(), ['a', 'b', 'c']))
[(0, 'a'), (1, 'b'), (2, 'c')]
```

### Recurent relations

A recurrence relation is a way of describing a sequence of numbers with a recursive formula (Fibonacci seq).
```markdown
def fibs():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```
`count_by_three = it.count(step=3)`

#### repeat()

Infinite
```markdown
all_ones = it.repeat(1)  # 1, 1, 1, 1, ...
all_twos = it.repeat(2)  # 2, 2, 2, 2, ...
```
Finite
```markdown
five_ones = it.repeat(1, 5)  # 1, 1, 1, 1, 1
three_fours = it.repeat(4, 3)  # 4, 4, 4
```
The primary purpose of `itertools.repeat` is to supply a stream of constant values to be used with `map` or `zip`:
```markdown
>>> list(map(pow, range(10), repeat(2)))     # list of squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Secondly, it gives a very fast way to loop a fixed number of times like this:

```markdown
for _ in itertools.repeat(None, 10000):
    do_something()
```
this is **faster** than:
```markdown
for i in range(10000):
    do_something()
```

The former wins because all it needs to do is update the reference count for the existing None object. The latter loses because the range() or xrange() needs to manufacture 10,000 distinct integer objects.

Guido fast looping technique:

```markdown
 if itertools:
        it = itertools.repeat(None, number)
    else:
        it = [None] * number
    gcold = gc.isenabled()
    gc.disable()
    try:
        timing = self.inner(it, self.timer)
```


#### cycle()

````markdown
alternating_ones = it.cycle([1, -1])  # 1, -1, 1, -1, 1, -1, ...
````

#### accumulate()

```markdown
def accumulate(inputs, func):
    itr = iter(inputs)
    prev = next(itr)
    for cur in itr:
        yield prev
        prev = func(prev, cur)
```

```markdown
>>> import operator
>>> list(it.accumulate([1, 2, 3, 4, 5], operator.add))
[1, 3, 6, 10, 15]
```
operator.add() is default, so this can be simplified

```markdown
list(it.accumulate([1, 2, 3, 4, 5]))
[1, 3, 6, 10, 15]
```
Keep track of running minimum
```markdown
>>> list(it.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min))
[9, 9, 9, 5, 5, 5, 2, 2]
```
with `lambda` expressions
```markdown
>>> list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: (x + y) / 2))
[1, 1.5, 2.25, 3.125, 4.0625]
```
Order is important
```markdown
>>> list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: x - y))
[1, -1, -4, -8, -13]

>>> list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: y - x))
[1, 1, 2, 2, 3]
```
#### First order

Ignore the second argument: `lambda x, _: p*s + q`

```markdown
def first_order(p, q, initial_val):
    """Return sequence defined by s(n) = p * s(n-1) + q."""
    return it.accumulate(it.repeat(initial_val), lambda s, _: p*s + q)
```

```markdown
>>> evens = first_order(p=1, q=2, initial_val=0)
>>> list(next(evens) for _ in range(5))
[0, 2, 4, 6, 8]

>>> odds = first_order(p=1, q=2, initial_val=1)
>>> list(next(odds) for _ in range(5))
[1, 3, 5, 7, 9]

>>> count_by_threes = first_order(p=1, q=3, initial_val=0)
>>> list(next(count_by_threes) for _ in range(5))
[0, 3, 6, 9, 12]

>>> count_by_fours = first_order(p=1, q=4, initial_val=0)
>>> list(next(count_by_fours) for _ in range(5))
[0, 4, 8, 12, 16]

>>> all_ones = first_order(p=1, q=0, initial_val=1)
>>> list(next(all_ones) for _ in range(5))
[1, 1, 1, 1, 1]

>>> all_twos = first_order(p=1, q=0, initial_val=2)
>>> list(next(all_twos) for _ in range(5))
[2, 2, 2, 2, 2]

>>> alternating_ones = first_order(p=-1, 0, initial_val=1)
>>> list(next(alternating_ones) for _ in range(5))
[1, -1, 1, -1, 1]
```
#### Second order

The difference here is that you need to create an intermediate sequence of tuples that keep track of the previous two elements of the sequence, and then map() each of these tuples to their first component to get the final sequence.
```markdown
def second_order(p, q, r, initial_values):
    """Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
    intermediate = it.accumulate(
        it.repeat(initial_values),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    return map(lambda x: x[0], intermediate)
```
Fibonacci
```markdown
>>> fibs = second_order(p=1, q=1, r=0, initial_values=(0, 1))
>>> list(next(fibs) for _ in range(8))
[0, 1, 1, 2, 3, 5, 8, 13]
```
Pell numbers
```markdown
pell = second_order(p=2, q=1, r=0, initial_values=(0, 1))
>>> list(next(pell) for _ in range(6))
[0, 1, 2, 5, 12, 29]
```
Lucas numbers
```
>>> lucas = second_order(p=1, q=1, r=0, initial_values=(2, 1))
>>> list(next(lucas) for _ in range(6))
[2, 1, 3, 4, 7, 11]
```
Alternating Fibonacci
```markdown
>>> alt_fibs = second_order(p=-1, q=1, r=0, initial_values=(-1, 1))
>>> list(next(alt_fibs) for _ in range(6))
[-1, 1, -2, 3, -5, 8]
```

### Deck of card

[cards.py](cards.py)

#### product()

Takes any number of iterables as arguments and returns an iterator over tuples in the Cartesian product.

```markdown
it.product([1, 2], ['a', 'b'])  # (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')
```
#### tee()

can be used to create any number of independent iterators from a single iterable

```markdown
>>> iterator1, iterator2 = it.tee([1, 2, 3, 4, 5], 2)
>>> list(iterator1)
[1, 2, 3, 4, 5]
>>> list(iterator1)  # iterator1 is now exhausted.
[]
>>> list(iterator2)  # iterator2 works independently of iterator1
[1, 2, 3, 4, 5].
```

 If you are exhausting large portions of an iterator before working with the other returned by tee(), you may be better off casting the input iterator to a list or tuple.

#### islice()

```markdown
>>> # Slice from index 2 to 4
>>> list(it.islice('ABCDEFG', 2, 5)))
['C' 'D' 'E']

>>> # Slice from beginning to index 4, in steps of 2
>>> list(it.islice([1, 2, 3, 4, 5], 0, 5, 2))
[1, 3, 5]

>>> # Slice from index 3 to the end
>>> list(it.islice(range(10), 3, None))
[3, 4, 5, 6, 7, 8, 9]

>>> # Slice from beginning to index 3
>>> list(it.islice('ABCDE', 4))
['A', 'B', 'C', 'D']
```

#### chain()

```markdown
>>> list(it.chain('ABC', 'DEF'))
['A' 'B' 'C' 'D' 'E' 'F']

>>> list(it.chain([1, 2], [3, 4, 5, 6], [7, 8, 9]))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Flattening A List of Lists

```markdown
>>> list(it.chain.from_iterable([[1, 2, 3], [4, 5, 6]]))
[1, 2, 3, 4, 5, 6]
```

```
>>> cycle = it.chain.from_iterable(it.repeat('abc'))
>>> list(it.islice(cycle, 8))
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']
```

### Analyzing the S&P500

[s_and_p_500.py](s_and_p_500.py)

#### functools.reduce()

Accepts a binary function func and an iterable inputs as arguments,
and “reduces” inputs to a single value by applying func cumulatively to pairs of objects in the iterable.
`functools.reduce(operator.add, [1, 2, 3, 4, 5])` will return the `sum 1 + 2 + 3 + 4 + 5 = 15.`
Working in much the same way as accumulate(), except that it returns only the final value in the new sequence.

#### filterfalse()

takes two arguments: a function that returns `True` or `False` (called a predicate), and an iterable inputs.
 It returns an iterator over the elements in inputs for which the predicate returns `False`.

```markdown
>>> only_positives = it.filterfalse(lambda x: x <= 0, [0, 1, -1, 2, -2])
>>> list(only_positives)
[1, 2]
```

To avoid of empty sequence pass `0` to reduce() as third argument:

```markdown
>>> ft.reduce(max, it.filterfalse(lambda x: x <= 0, [-1, -2, -3]), 0)
0
```

#### takewhile() and dropwhile() 

The 'takewhile()' function takes a predicate and an iterable inputs as arguments and returns an iterator over inputs that
stops at the first instance of an element for which the predicate returns 'False':


```markdown
it.takewhile(lambda x: x < 3, [0, 1, 2, 3, 4])  # 0, 1, 2
```

The `dropwhile()` function does exactly the opposite.
It returns an iterator beginning at the first element for which the predicate returns `False`

```markdown
t.dropwhile(lambda x: x < 3, [0, 1, 2, 3, 4])  # 3, 4
```

### Swimmer teams
[swimmers.py](swimmers.py)

#### groupby()

takes an iterable inputs and a key to group by, and returns an object containing iterators over the elements of inputs grouped by the key

```markdown
>>> data = [{'name': 'Alan', 'age': 34},
...         {'name': 'Catherine', 'age': 34},
...         {'name': 'Betsy', 'age': 29},
...         {'name': 'David', 'age': 33}]
...
>>> grouped_data = it.groupby(data, key=lambda x: x['age'])
>>> for key, grp in grouped_data:
...     print('{}: {}'.format(key, list(grp)))
...
34: [{'name': 'Alan', 'age': 34}, {'name': 'Betsy', 'age': 34}]
29: [{'name': 'Catherine', 'age': 29}]
33: [{'name': 'David', 'age': 33}]
```

`groupby()` defaults to grouping by “identity”—that is, aggregating identical elements in the iterable:

```markdown
>>> for key, grp in it.groupby([1, 1, 2, 2, 2, 3]:
...     print('{}: {}'.format(key, list(grp)))
...
1: [1, 1]
2: [2, 2, 2]
3: [3]
```
`groupby()` returns an iterator over tuples whose first components are keys and second components are iterators over the grouped data

```markdown
>>> grouped_data = it.groupby([1, 1, 2, 2, 2, 3])
>>> list(grouped_data)
[(1, <itertools._grouper object at 0x7ff3056130b8>),
 (2, <itertools._grouper object at 0x7ff3056130f0>),
 (3, <itertools._grouper object at 0x7ff305613128>)]
```

