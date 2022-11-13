import os
from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        name = old_function.__name__
        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(f'{str(datetime.today())}\n')
            f.write(f'{str(name)}\n')
            for a_el in args:
                f.write(f'{str(a_el)}\n')
            for k, v in kwargs.items():
                f.write(f'{k, v}\n')
            res = old_function(*args, **kwargs)
            f.write(f'{str(res)}\n')
            return res

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def summator(a, b=0):
        return a + b

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
