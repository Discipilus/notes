# Python

#### Python own package
```bash
# make archive package to dist
> python setup.py sdist
> pip install dist/edx_localization_ext-1.0.tar.gz
# install without creating package
> python setup.py install
```

#### numpy
```python
# Split an array into multiple sub-arrays.
numpy.array_split(array, number_of_subarrays)
```

#### Install python from source
```bash
sudo apt update
sudo apt upgrade
sudo apt install libffi-dev

git clone https://github.com/python/cpython.git
cd cpython
mkdir bin
cd bin
../configure --with-ensurepip=install --enable-optimizations
make -j <CPU cores number>
sudo make altinstall

python3.11 -m venv
```

#### Json
```
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        return obj

json_course_block_tree = json.dumps(course_block_tree, cls=ComplexEncoder)
```


#### Build wheel package
```bash
python setup.py bdist_wheel
```

#### Download packages
```bash
pip download -d /home/ad/Projects/big3/app-back/GDAL GDAL
```

#### Processes
```python
from pathlib import Path

def subp(*args):
    import tempfile
    import subprocess
    import time
    print(f'ARGS: {args}')
    d = '/home/ad/Projects/big3/tmp/storage/'
    tmp_dir = tempfile.mkdtemp(dir=d)
    print(tmp_dir)
    proc_args = f'soffice --headless --convert-to pdf --outdir {tmp_dir} {d}/0bb4ab6173ed47509a373914a7a57933.docx'.split()

    p = Path(tmp_dir)
    while len(list(p.glob('*.pdf'))) == 0:
        try:
            print(f'Start process {args[0]}')
            proc = subprocess.Popen(proc_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=False)
            out, err = proc.communicate(timeout=20)
            print(out, err)
        except subprocess.TimeoutExpired:
            print(f'ERROR: Timeout process {args[0]}')
            raise
    print(list(p.glob('*.pdf')))


def f():
    from multiprocessing import Pool, Process
    with Pool(processes=5) as p:
        p.map(subp, range(10))
```


### Closures
```python
def f():
    a = 1
    ttt = [1,2,3]
    sss = '123'
    def f2(b):
        ttt_l = ttt
        sss_l = sss
        return a + b
    return f2


g = f()


In [53]: g.__code__.co_freevars
Out[53]: ('a', 'sss', 'ttt')

In [54]: g.__closure__
Out[54]: 
(<cell at 0x7fa2e3cb9f00: int object at 0xaaa308>,
 <cell at 0x7fa2e3cb8850: str object at 0x7fa2f00b19f0>,
 <cell at 0x7fa2e3cb84f0: list object at 0x7fa2e3b650c0>)

In [57]: g.__closure__[0].cell_contents
Out[57]: 1

In [58]: g.__closure__[1].cell_contents
Out[58]: '123'

In [59]: g.__closure__[2].cell_contents
Out[59]: [1, 2, 3]

In [60]: g.__code__.co_varnames
Out[60]: ('b', 'ttt_l', 'sss_l')
```

### Nonlocal
```python
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

In [62]: avg = make_averager()

In [63]: avg.__closure__
Out[63]: 
(<cell at 0x7fa2e3a47ac0: int object at 0xaaa2e8>,
 <cell at 0x7fa2e3a449d0: int object at 0xaaa2e8>)

In [64]: avg.__closure__[0]
Out[64]: <cell at 0x7fa2e3a47ac0: int object at 0xaaa2e8>

In [65]: avg.__closure__[0].cell_contents
Out[65]: 0

In [66]: avg.__closure__[1].cell_contents
Out[66]: 0

In [67]: avg.__code__.co_freevars
Out[67]: ('count', 'total')

In [68]: avg.__code__.co_varnames
Out[68]: ('new_value',)
```

### Time meausre
#### Performance counter for benchmarking
```python
t0 = time.perf_counter()
total = time.perf_counter() - t0
```


### Celery
#### Run tasks synchronously
```bash
CELERY_ALWAYS_EAGER = True
CELERY_TASK_ALWAYS_EAGER = True	# > 4.0 version
```

#### Tasks
###### For the newer versions of celery(4.0 or above), we can get registered tasks as follows.
```python
from celery import current_app 
tasks = current_app.tasks.keys()
```

#### For older versions of celery, celery < 4, we can get registered tasks as follows.
```python
from celery.task.control import  inspect
i = inspect()
i.registered_tasks()
```

```python
# This will give a dictionary of all workers & related registered tasks.
from itertools import chain
set(chain.from_iterable( i.registered_tasks().values() ))
```


# Django
```python
from django.db.models import Count, Max, Avg

## Annotate
for u in User.objects.all().annotate(bc_count=Count('blockcompletion')):
   print(u.bc_count)


## Aggregate
In [49]: BlockCompletion.objects.all().aggregate(my_compl=Max('completion'))
Out[49]: {'my_compl': 1.0}


## Group by
In [60]: TopicEntities.objects.filter(id__in=topic_ids,
    ...:                              entity=ENTITY_TYPES[ATTENDANCE_ENTITY_TYPE]
    ...:                             ).values('entity').annotate(entries=Count('entity'))
Out[60]: <QuerySet [{'entries': 73, 'entity': u'ATTENDANCE'}]>


#### Django:
DocStatusTransition.objects.values('code', 'doc_type__code').annotate(code_count=Count('code'), doc_type__code_count=Count('doc_type__code')).filter(doc_type__code_count__gt=1)

##### The same with SQL:
SELECT 
    "workflow_docstatustransition"."code", 
    "workflow_doctype"."code", 
    COUNT("workflow_docstatustransition"."code") AS "code_count", 
    COUNT("workflow_doctype"."code") AS "doc_type__code_count" 
FROM "workflow_docstatustransition" 
INNER JOIN "workflow_doctype" ON ("workflow_docstatustransition"."doc_type_id" = "workflow_doctype"."id") 
GROUP BY "workflow_docstatustransition"."code", 
         "workflow_doctype"."code" 
HAVING COUNT("workflow_doctype"."code") > 1';


## Check if we are in atomic block
if transaction.get_connection().in_atomic_block:
    transaction.on_commit(lambda: create_documents(obj, self))
else:
    create_documents(obj, self)
```

#### Widgets
###### Calendar in admin panel
```python
from django.forms import DateInput

class DateInputWithCalendar(DateInput):
    input_type = 'date'
```


# External Libraries

## GDAL
```bash
RUN cd / && \
    unzip linux-amd64_for_pycades.zip && \
    chmod +x linux-amd64_for_pycades/install.sh && \
    linux-amd64_for_pycades/install.sh && \
    cd linux-amd64_for_pycades/ && apt-get install -y ./lsb-cprocsp-devel_5.0.12600-6_all.deb && \
    cd / && tar xvf cades-linux-amd64.tar.gz && \
    cd /cades-linux-amd64/ && apt-get install -y ./cprocsp-pki-cades-64_2.0.14660-1_amd64.deb && \
    cd / && unzip pycades.zip && cd ./pycades && mkdir build && cd build && cmake .. && make -j4 && \
    mkdir /opt/cprocsp/bin/amd64/pycades_lib && cp ./pycades.so /opt/cprocsp/bin/amd64/pycades_lib/
```

```bash
gdal-config --version
gdal-config --cflags
```

Here we get path where C/C++ headers are located
Setup envs with this path:
```bash
export CPLUS_INCLUDE_PATH=/usr/local/include/
export C_INCLUDE_PATH=/usr/local/include/
``` 

Build GDAL:
```bash
cmake -DPython_LOOKUP_VERSION=3.11 ..
cmake --build .
sudo cmake --build . --target install
```

# Python dependencies


# Python checkers
### [Pylint](https://pypi.org/project/pylint/)
```bash
pip install pylint
```

### [Flake8](https://pypi.org/project/flake8/)

Flake8 is a wrapper around these tools:
- PyFlakes
- pycodestyle
- Ned Batchelder’s McCabe script

```
pip install flake8
```

### [mypy](https://pypi.org/project/mypy/) 
Add type annotations to your Python programs, and use mypy to type check them. Mypy is essentially a Python linter on steroids, and it can catch many programming errors by analyzing your program, without actually having to run it. Mypy has a powerful type system with features such as type inference, gradual typing, generics and union types

```
pip install mypy
```
[https://mypy.readthedocs.io/en/stable/getting_started.html](https://mypy.readthedocs.io/en/stable/getting_started.html)

```shell
flake8 . ; mypy . ; find . -name '*.py' -exec pylint {} \;
```

### [RUFF](https://pypi.org/project/ruff/)

[https://beta.ruff.rs/docs/tutorial/#getting-started](https://beta.ruff.rs/docs/tutorial/#getting-started)

```shell
pip install ruff
ruff check <directory with python code>
```

### [Pyrighth](https://pypi.org/project/pyright/)
```
pip install pyright
```



