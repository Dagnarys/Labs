

# Подключаем библиотеку unitetest для тестирования
import unittest

from unique import Unique

'''
assertEqual(self, first, second)
first - передаваемое значение
second - полученное значение (в тело функции должен быть return, если вы там не оставили, тогда прописать здесь как None)
если передаваемое значение совпадает с полученным значением, то тест пройден успешно
'''


class test_unique(unittest.TestCase):
    def test_value(self):
        data = [1, 1, 1, 2, 2, 2, 3, 3, 4]
        arr_unique = list(Unique(data))

        self.assertEqual(arr_unique, [1, 2, 3, 4])

    def test_val(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        # Получаем уникальные значения и сохраним его в переменной
        arr_unique = list(Unique(data))
        # Проверяем
        self.assertEqual(
            arr_unique,
            ['a', 'A', 'b', 'B']
        )

    def test_val_ignore_case(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        # Получаем уникальные значения и сохраним его в переменной
        arr_unique = list(Unique(data, ignore_case=True))
        # Проверяем
        self.assertEqual(
            arr_unique,
            ['a', 'b']
        )


if __name__ == '__main__':
    unittest.main()