# Multiple assignments

### Replace hard coded indexes
Instead of:
```
def reformat_date(mdy_date_string):
    """Reformat MM/DD/YYYY string into YYYY-MM-DD string."""
    date = mdy_date_string.split('/')
    return f"{date[2]}-{date[0]}-{date[1]}"
```
Consider:
```
def reformat_date(mdy_date_string):
    """Reformat MM/DD/YYYY string into YYYY-MM-DD string."""
    month, day, year = mdy_date_string.split('/')
    return f"{year}-{month}-{day}"
```
If we use multiple assignment instead of hard coded indexes, the assignment will verify that we receive exactly the expected number of arguments:
```
import sys

_, new_file, old_file = sys.argv
print(f"Copying {new_file} to {old_file}")

```

we’re using the variable name `_` to note that we don’t care about `sys.argv[0]` (the name of our program).

### Alternative to slicing

```
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> first, *rest = numbers
>>> rest
[2, 3, 4, 5, 6]
>>> first
1
```
Equivalent lines
```
>>> head, middle, tail = numbers[0], numbers[1:-1], numbers[-1]
>>> head, *middle, tail = numbers
```
Instead of:
```
main(sys.argv[0], sys.argv[1:])
```
Consider:
```
program_name, *arguments = sys.argv
main(program_name, arguments)

```
### Deep unpacking

```
>>> color, (x, y, z) = ("red", (1, 2, 3))
>>> color
'red'
>>> x
1
>>> y
2
```

Instead of:

```
start_points = [(1, 2), (3, 4), (5, 6)]
end_points = [(-1, -2), (-3, 4), (-6, -5)]

for start, end in zip(start_points, end_points):
    if start[0] == -end[0] and start[1] == -end[1]:
        print(f"Point {start[0]},{start[1]} was negated.")
```

Consider:
```
for (x1, y1), (x2, y2) in zip(start_points, end_points):
    if x1 == -x2 and y1 == -y2:
        print(f"Point {x1},{y1} was negated.")
```

Using `enumerate` and `zip` together:

```
items = [1, 2, 3, 4, 2, 1]
for i, (first, last) in enumerate(zip(items, reversed(items))):
    if first != last:
        raise ValueError(f"Item {i} doesn't match: {first} != {last}")
```
Good example
```
>>> points = ((1, 2), (-1, -2))
>>> points = ((1, 2), (-1, -2))
>>> (x1, y1), (x2, y2) = points
>>> x1 == -x2 and y1 == -y2
True
```
### List-like syntax

```
def most_common(items):
    [(value, times_seen)] = Counter(items).most_common(1)
    return value
```