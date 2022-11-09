class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self._data = items
        self._ignore_case = ignore_case
        self._used_data = set()
        self._index = 0

    def __next__(self):
        if self._ignore_case:
            for count, el in enumerate(self._data):
                if type(el) is str:
                    self._data[count] = el.lower()
        while True:
            if self._index >= len(self._data):
                raise StopIteration
            else:
                current = self._data[self._index]
                self._index += 1
                if current not in self._used_data:
                    self._used_data.add(current)
                    return current

    def __iter__(self):
        return self


def main_unique():
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    ex = Unique(data, ignore_case=True)
    try:
        while True:
            print(ex.__next__())
    except StopIteration:
        print('Error "StopIteration"')


if __name__ == '__main__':
    main_unique()