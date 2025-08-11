import pytest


@pytest.mark.xfail(reason="Баг с 1 == 2")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг уже исправлен")
def test_without_bug():
    ...

