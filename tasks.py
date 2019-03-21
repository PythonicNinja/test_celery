from sys import argv

import datetime as dt

from celery.task


def formula(x, y):
    task1 = multiply.apply_async((x, y), countdown=10)
    task2 = save_to_file.apply_async((x, dt.datetime.now().isoformat(), 'formula'), countdown=10)
    taskset = TaskSet
    return task1, task2


@app.task
def save_to_file(value, ts, function_name):
    with open('/Users/pythonicninja/PycharmProjects/test_celery/out.txt', 'a') as output_file:
        output_file.writelines("[{2}]{0} - {1}".format(ts, value, function_name))


@app.task
def multiply(x, y):
    saved_value = save_to_file.apply_async((x, dt.datetime.now().isoformat(), 'multiply'), countdown=10)
    return plus1.apply_async((x * y,), countdown=10)


@app.task
def plus1(x):
    saved_value = save_to_file.apply_async((x, dt.datetime.now().isoformat(), 'plus1'), countdown=10)
    return x + 1


if __name__ == '__main__':
    values = map(int, [argv[1], argv[2]])
    print(formula(*values))
