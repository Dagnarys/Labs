from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
import json
import sys

try:
    path = sys.argv[1]
    print(path)
except:
    path = 'data_light.json'

with open(path, encoding='UTF-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return list(Unique([i for i in field(arg, 'job-name')], ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda s: (s.split())[0].lower() == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda k: k + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(zip(arg, ['зарплата ' + str(el) + ' руб.' for el in gen_random(len(arg), 100000, 200000)]))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
