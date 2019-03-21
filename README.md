# test_celery

```
virtualenv env -p python3
pip install celery
```


# run worker

```
celery worker --app celeryd --loglevel DEBUG
```


# add task to worker

```
python tasks.py 2 6
```

or

```
>>> from tasks import *
>>> multiply.apply_async((2, 6))
<AsyncResult: 2b5539c6-e970-4e2a-9f99-f1ae62ef93d8>
>>> task = multiply.apply_async((2, 6))
```