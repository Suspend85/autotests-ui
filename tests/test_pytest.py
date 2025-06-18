def test_user_login():
    print('hello')


class TestUserLogin:
    # в pytest не должно быть конструкторов
    # def __init__(self):
    #     ...
    # запуск тестов командой: python -m pytest -s -v -k "test_user_login or test_1"

    def test_1(self):
        ...

    def test_2(self):
        ...


def test_assert_positive_case():
    assert (2 + 2) == 4
    assert (3 + 3) == 6
    assert (4 + 4) == 8


def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) != 5"
