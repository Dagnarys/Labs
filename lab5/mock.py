from unittest import mock
from unittest import TestCase

class Test(TestCase):
    @mock.patch('mock.sum',return_value=8)
    def test(self ,mock_check_output):
        result = main()
        expect_result = 8
        self.assertEqual(expect_result,result)

def sum(a,b):
    return a+b

def main():

    s = sum(3, 5)
    return s

if __name__ == '__main__':
    main()