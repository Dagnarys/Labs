from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __int__(self):
        self._start = 0
        self._end = 0

    def __enter__(self):
        self._start = time()

    def __exit__(self, the_type, the_value, the_backing):
        self._end = time()
        print(f'Time of work: {self._end - self._start}')


@contextmanager
def cm_timer_2():
    start_time = time()
    yield None
    end_time = time()
    print(f'Time of work: {end_time - start_time}')


def main_cm_timer():
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)


if __name__ == '__main__':
    main_cm_timer()
