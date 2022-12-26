import unittest
import os.path



class test_telebot(unittest.TestCase):

    # Проверка создания файла
    def test_create_file_json(self):

        self.assertEqual(
            os.path.exists('json.json'),
            True
        )

    def test_create_file_photo(self):

        self.assertEqual(
            os.path.exists('photo.jpg'),
            True
        )


