def field(items, *args):
    assert len(args) > 0
    arr = []
    if len(args) == 1:
        for item in items:
            for el in item:
                if el == args[0] and item[el] is not None:
                    arr.append(item[el])
        return arr
    else:
        for item in items:
            for_dict = dict()
            for el in item:
                for argument in args:
                    if el == argument and item[argument] is not None:
                        for_dict[el] = item[el]
            arr.append(for_dict)
        return arr


def main_field():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    res = field(goods, 'title')
    for el in res:
        print(el)
    res1 = field(goods, 'title', 'price')
    for el in res1:
        print(el)



if __name__ == '__main__':
    main_field()
