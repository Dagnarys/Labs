def print_result(function):
    def control(arr=[], *args, **kwargs):
        print(function.__name__)
        if len(arr) == 0:
            result = function(*args, **kwargs)
        else:
            result = function(arr, *args, **kwargs)
        if type(result) == int or type(result) == str:
            print(result)
        elif type(result) is list:
            print('\n'.join(map(str, result)))
        elif type(result) is dict:
            for key, el in result.items():
                print(f'{key} = {el}')
        elif type(result) == zip:
            for name, number in result:
                print(name, number)
        else:
            print(result)
        return result

    return control


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main_print_result():
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main_print_result()
