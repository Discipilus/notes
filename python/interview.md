# Online editor
[Collabedit](https://collabedit.com/dyh98/)


# Python
- Dynamic Strongly Typed Language

- `l = [1, 44, 666, 123, 777, 3234, -123, 0, 2]`
  function which takes a list and returns new list with items more than 144
 
- `d = {'aaa': 111, 'bbb': 222, 'ccc': 333, 'eee': 444}`
   function returns new dict where values more than 200 and less than 400
   
- Decorator which measure method/function time execution and prints logs
   `@measure_exec_time(time_threshold: float = 1.0)`
```python
@measure_exec_time(1.0)
def add(a: int, b: int) -> int:
    return a + b
```
 
- Remove duplicates with ordering saving
```python
 >>> l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
 >>> l = ['spam', 'spam', 'eggs', 'eggs', 'bacon']
 >>> list(dict.fromkeys(l).keys())
```
 - mro
```python
class MyClass:
    class_var = 111
    def __init__(self, a, var):
        self._a = a
        self.class_var = var
mc = MyClass(222, 333)
mc.class_var
```

### Dynamic attrs in JS-style
```python
In [21]: class DynamicAttrs:
    ...:     def __init__(self, data: dict):
    ...:         self._data = data
    ...:     def __repr__(self):
    ...:         return str(self._data)
    ...:     def __getitem__(self, attr):
    ...:         return self._data[attr]
    ...:     def __getattr__(self, attr):
    ...:         if attr in self._data:
    ...:             cls = type(self)
    ...:             return cls(self._data[attr])
    ...:         raise KeyError(f'No such attr {attr} found')
    ...: 

In [22]: dyn = DynamicAttrs({'aaa': {'kkk': {'fff': 444}}})

In [23]: dyn
Out[23]: {'aaa': {'kkk': {'fff': 444}}}

In [24]: dyn.aaa
Out[24]: {'kkk': {'fff': 444}}

In [25]: dyn.aaa.kkk
Out[25]: {'fff': 444}

In [26]: dyn.aaa.kkk.fff
Out[26]: 444
```
 

# Tests
Waht do we need unit tests for?
Frameworks?
Fixtures


# Refactoring
```python
def calculate_daily_electricity_costs() -> float:
    from datetime import time, datetime
    day_price = 4.22  # per hour
    night_price = 2.34  # per hour
    
    t_day_start = time.fromisoformat('06:00')
    t_day_end = time.fromisoformat('18:00')
    
    current_time = datetime.now().time()
    
    if t_day_start < current_time <= t_day_end:
        before_day_costs = (t_day_start.hour + t_day_start.minute / 60) * night_price
        day_costs = (current_time.hour - t_day_start.hour 
                     + current_time.minute / 60 - t_day_start.minute / 60) * day_price
        total_costs = before_day_costs + day_costs
    elif current_time <= t_day_start:
        before_day_costs = (current_time.hour + current_time.minute / 60) * night_price
        total_costs = before_day_costs
    else:
        before_day_costs = (t_day_start.hour + t_day_start.minute / 60) * night_price
        day_costs = (t_day_end.hour - t_day_start.hour + t_day_end.minute / 60 - t_day_start.minute / 60) * day_price
        after_day_costs = (current_time.hour - t_day_end.hour 
                           + current_time.minute / 60 - t_day_end.minute / 60) * night_price
        total_costs = before_day_costs + day_costs + after_day_costs
    return total_costs
```



# Django

```python
class Author(models.Model):
    nickname = models.CharField('Author nickname', max_length=255, unique=True)
    first_name = models.CharField('Author first name', max_length=255)
    last_name = models.CharField('Author last name', max_length=255)


class Book(models.Model):
    title = models.CharField('Book title', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               verbose_name='Author', related_name='books')

books_list = [
    {
        'title': "Title one",
        'nickname': 'nickname1',
        'first_name': 'First1',
        'last_name': 'Last1'
    },
    {
        'title': "Title two",
        'nickname': 'nickname2',
        'first_name': 'First2',
        'last_name': 'Last2'
    },
    {
        'title': "Title three",
        'nickname': 'nickname3',
        'first_name': 'First3',
        'last_name': 'Last3'
    }
]
```

# Databases
ACID:
 - atomicity
  (In Django?)
 - consistency
 - Isolation
 - durability

Indexes


# Architesture
Hexagonal Architecture, DDD, SOLID
# Process


# GIT
```
git add
git commit
git checkout
git reset
git merge
git rebase
git push
git checkout
git branch

```

# Docker





