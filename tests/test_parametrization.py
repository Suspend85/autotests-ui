
import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -2])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser {browser}')


# Для тестовых классов параметризациф указывается для самого класса
@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


users = {
    '+79131231111': 'User with money in bank account',
    '+79131231122': 'User without money on bank account',
    '+79131231133': 'User with operations on bank account'
}


def format_phone_number(phone_number: str) -> str:
    return f'{phone_number}: {users[phone_number]}'


@pytest.mark.parametrize(
    'phone_number', users.keys(),
    ids=format_phone_number
    # Генерируем идентификаторы динамически
    # ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...
