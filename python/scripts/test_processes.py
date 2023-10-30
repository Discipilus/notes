#!/usr/bin/env python

from multiprocessing import Process
from time import sleep


def test_func(*args, **kwargs):
    print(args, kwargs)
    sleep(30)


def run_processes():
    processes = []
    for i in range(10):
        process = Process(target=test_func, args=(i + 1, i + 11),
                          kwargs={f'a{i}': i + 111, f'b{i}': i + 1111})
        process.start()
        processes.append(process)

    for p in processes:
        p.join()


if __name__ == '__main__':
    run_processes()
