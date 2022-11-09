from random import randint


def gen_random(count, first, last):
    return (randint(first, last) for _ in range(count))


def main_gen_random():
    numbers = gen_random(4, 0, 5)
    for el in numbers:
        print(el, end=' ')


if __name__ == '__main__':
    main_gen_random()
