#!/usr/bin/env python

from threading import Thread
from time import sleep


def test_func(*args, **kwargs):
    print(args, kwargs)
    sleep(30)


def run_threads():
    threads = []
    for i in range(10):
        thread = Thread(target=test_func, args=(i + 1, i + 11), kwargs={f'a{i}': i + 111, f'b{i}': i + 1111})
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()


if __name__ == '__main__':
    run_threads()
