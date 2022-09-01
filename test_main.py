import pytest
from main import *

test = [('llm@gmail.com', 1), ('ll.a', 0), ('m_l.c@hotmail.fr', 1)]
@pytest.mark.parametrize('sample, expected', test)
def test_email(sample, expected):
    assert is_email(sample) == expected

def test_is_username_not_empty():
    assert not is_username('')

def test_is_username_no_space():
    assert not is_username('mo ou')
    assert not is_username(' mo')
    assert not is_username('mo ')
    assert is_username('mo1')

def test_is_username_alphanumeric():
    assert not is_username('mo_ou1')
    assert not is_username('.mo')

def test_is_password_8_char():
    assert not is_password('ma1lma2')